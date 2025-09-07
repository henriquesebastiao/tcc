from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect, status

from server.db import redis_client
from server.hasher import hash_id
from server.logger import logger
from server.schemas.ws import RecipientAvailabilitySchema

router = APIRouter(prefix='/ws', tags=['WebSocket'])

active_connections: dict[str, WebSocket] = {}
active_tunnels = set()
waiting_for: dict[str, list[str]] = {}
tunnel_users: dict[frozenset, set[str]] = {}

async def cleanup_user_from_redis(user_id: str):
    await redis_client.srem('online_users', user_id)
    logger.info(f'Usuário {user_id} removido do Redis.')


async def handle_user_disconnect(disconnected_user: str, tunnel_id: frozenset):
    if disconnected_user in active_connections:
        del active_connections[disconnected_user]

    await cleanup_user_from_redis(disconnected_user)

    if tunnel_id in tunnel_users:
        tunnel_users[tunnel_id].discard(disconnected_user)

        remaining_users = tunnel_users[tunnel_id].copy()
        for user_id in remaining_users:
            if user_id in active_connections:
                try:
                    await active_connections[user_id].send_text(
                        'system-message: O outro usuário se desconectou.'
                    )
                    await active_connections[user_id].close()

                    del active_connections[user_id]
                    await cleanup_user_from_redis(user_id)

                except Exception as e:
                    logger.error(f'Erro ao notificar usuário {user_id}: {e}')
                    if user_id in active_connections:
                        del active_connections[user_id]
                    await cleanup_user_from_redis(user_id)

        del tunnel_users[tunnel_id]
        if tunnel_id in active_tunnels:
            active_tunnels.remove(tunnel_id)

    if disconnected_user in waiting_for:
        del waiting_for[disconnected_user]

    for recipient, senders in waiting_for.items():
        if disconnected_user in senders:
            senders.remove(disconnected_user)


@router.get(
    '/check-availability/{recipient_id}',
    response_model=RecipientAvailabilitySchema,
    summary='Retorna se destinatário já está conectado com algum usuário',
)
async def check_recipient_availability(recipient_id: str):
    hashed_recipient = hash_id(recipient_id)
    recipient_online = await redis_client.sismember('online_users', hashed_recipient)

    if recipient_online and hashed_recipient in active_connections:
        for tunnel_id, users in tunnel_users.items():
            if hashed_recipient in users and len(users) > 1:
                raise HTTPException(
                    status_code=status.HTTP_423_LOCKED,
                    detail='Destinatário já está em uma conversa ativa',
                )

    data = {
        'recipient_online': bool(recipient_online),
        'message': 'Destinatário disponível para conexão',
    }

    return data


@router.websocket('/{sender_id}@{recipient_id}')
async def websocket_endpoint(websocket: WebSocket, sender_id: str, recipient_id: str):
    sender_id = hash_id(sender_id)
    recipient_id = hash_id(recipient_id)
    await websocket.accept()

    if sender_id == recipient_id:
        await websocket.send_text('system-error: Você não pode se conectar com você mesmo.')
        await websocket.close()
        return

    is_online = await redis_client.sismember('online_users', sender_id)
    if is_online:
        await websocket.send_text(
            'system-error: Já há um usuário conectado com o ID que você solicitou.'
        )
        await websocket.close()
        return

    if recipient_id in active_connections:
        for tunnel_id, users in tunnel_users.items():
            if recipient_id in users and len(users) > 1:
                await websocket.send_text(
                    'system-error: O destinatário já está em uma conversa ativa.'
                )
                await websocket.close()
                return

    active_connections[sender_id] = websocket
    await redis_client.sadd('online_users', sender_id)
    tunnel_id = frozenset({sender_id, recipient_id})
    active_tunnels.add(tunnel_id)

    if tunnel_id not in tunnel_users:
        tunnel_users[tunnel_id] = set()
    tunnel_users[tunnel_id].add(sender_id)

    if recipient_id in active_connections:
        tunnel_users[tunnel_id].add(recipient_id)

    logger.info(f'Usuário {sender_id} conectado.')

    if recipient_id not in active_connections:
        waiting_for.setdefault(recipient_id, []).append(sender_id)

        await websocket.send_text(
            'system-message: O destinatário ainda não está conectado. '
            'Você será notificado quando ele estiver online.'
        )

    if sender_id in waiting_for:
        for waiting_sender in waiting_for[sender_id]:
            if waiting_sender in active_connections:
                await active_connections[waiting_sender].send_text(
                    'system-message: O usuário destinatário agora está conectado.'
                )
                tunnel_users[tunnel_id].add(waiting_sender)
        del waiting_for[sender_id]

    try:
        while True:
            message = await websocket.receive_text()

            if recipient_id in active_connections:
                await active_connections[recipient_id].send_text(message)
            else:
                await websocket.send_text(
                    'system-message: O outro usuário ainda não está conectado.'
                )

    except WebSocketDisconnect:
        logger.info(f'Usuário {sender_id} desconectado.')
        await handle_user_disconnect(sender_id, tunnel_id)
