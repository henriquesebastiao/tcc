import asyncio
import base64

import websockets
from confy_addons.encryption import (
    aes_decrypt,
    aes_encrypt,
    deserialize_public_key,
    generate_aes_key,
    generate_rsa_keypair,
    rsa_decrypt,
    rsa_encrypt,
    serialize_public_key,
)
from confy_addons.prefixes import AES_KEY_PREFIX, AES_PREFIX, KEY_EXCHANGE_PREFIX, SYSTEM_PREFIX
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from confy.utils import get_protocol, is_prefix


class WebSocketThread(QThread):
    message_received = Signal(str, str)
    connection_status = Signal(str)
    system_message = Signal(str)
    error_occurred = Signal(str)

    def __init__(self, server_address, user_id, recipient_id):
        super().__init__()

        self.server_address = server_address
        self.user_id = user_id
        self.recipient_id = recipient_id
        self.running = True
        self.websocket = None

        self.private_key, self.public_key = generate_rsa_keypair()

        self.peer_public_key = None
        self.peer_aes_key = None

        self.public_sent = False

        self.message_queue = asyncio.Queue()

    def run(self):
        asyncio.run(self.websocket_client())

    async def websocket_client(self):
        protocol, host = get_protocol(self.server_address)
        uri = f'{protocol}://{host}/ws/{self.user_id}@{self.recipient_id}'

        try:
            async with websockets.connect(uri) as websocket:
                self.websocket = websocket
                self.connection_status.emit('Conectado')

                receive_task = asyncio.create_task(self.receive_messages())
                send_task = asyncio.create_task(self.process_send_queue())

                done, pending = await asyncio.wait(
                    [receive_task, send_task], return_when=asyncio.FIRST_COMPLETED
                )

                for task in pending:
                    task.cancel()

        except Exception as e:
            self.error_occurred.emit(f'Erro de conexão: {str(e)}')
        finally:
            self.connection_status.emit('Desconectado')

    async def receive_messages(self):
        try:
            while self.running:
                try:
                    message = await self.websocket.recv()
                except websockets.ConnectionClosed:
                    self.running = False
                    self.connection_status.emit('Conexão fechada')
                    break

                await self.process_received_message(message)

        except Exception as e:
            self.error_occurred.emit(f'Erro ao receber mensagem: {str(e)}')

    async def process_received_message(self, message):

        if is_prefix(message, SYSTEM_PREFIX):
            if message == f'{SYSTEM_PREFIX} O usuário destinatário agora está conectado.':
                if not self.public_sent:
                    pub_b64 = serialize_public_key(self.public_key)
                    await self.websocket.send(f'{KEY_EXCHANGE_PREFIX}{pub_b64}')
                    self.public_sent = True

            self.system_message.emit(message)
            return

        elif is_prefix(message, KEY_EXCHANGE_PREFIX):
            b64_key = message[len(KEY_EXCHANGE_PREFIX) :]
            try:
                self.peer_public_key = deserialize_public_key(b64_key)
            except Exception as e:
                self.error_occurred.emit(f'Chave pública do peer inválida: {e}')
                return

            if not self.public_sent:
                try:
                    pub_b64 = serialize_public_key(self.public_key)
                    await self.websocket.send(f'{KEY_EXCHANGE_PREFIX}{pub_b64}')
                    self.public_sent = True
                except Exception as e:
                    self.error_occurred.emit(f'Falha ao enviar chave pública: {e}')
                    return

            if self.peer_aes_key is None and self.public_sent:
                should_generate = str(self.user_id) > str(self.recipient_id)
                if should_generate:
                    aes_key = generate_aes_key()
                    encrypted_key = rsa_encrypt(self.peer_public_key, aes_key)
                    b64_encrypted_key = base64.b64encode(encrypted_key).decode()
                    await self.websocket.send(f'{AES_KEY_PREFIX}{b64_encrypted_key}')
                    self.peer_aes_key = aes_key

        elif is_prefix(message, AES_KEY_PREFIX):
            b64_enc = message[len(AES_KEY_PREFIX) :]
            try:
                encrypted_key = base64.b64decode(b64_enc)
                aes_key = rsa_decrypt(self.private_key, encrypted_key)
                self.peer_aes_key = aes_key
                self.system_message.emit('Chave AES estabelecida - comunicação segura ativa')
            except Exception as e:
                self.error_occurred.emit(f'Falha ao descriptografar a chave AES: {e}')
            return

        elif is_prefix(message, AES_PREFIX):
            if self.peer_aes_key is None:
                self.system_message.emit(
                    'Mensagem criptografada recebida, mas chave AES não definida'
                )
                return

            b64_payload = message[len(AES_PREFIX) :]
            try:
                decrypted = aes_decrypt(self.peer_aes_key, b64_payload)
                self.message_received.emit(self.recipient_id, decrypted)
            except Exception as e:
                self.error_occurred.emit(f'Falha ao descriptografar mensagem: {e}')
        else:
            self.message_received.emit(self.recipient_id, message)

    async def process_send_queue(self):
        while self.running:
            try:
                message = await asyncio.wait_for(self.message_queue.get(), timeout=1.0)
                await self.send_encrypted_message(message)
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                self.error_occurred.emit(f'Erro ao enviar mensagem: {str(e)}')

    async def send_encrypted_message(self, message):
        if self.peer_aes_key:
            try:
                encrypted_payload = aes_encrypt(self.peer_aes_key, message)
                await self.websocket.send(f'{AES_PREFIX}{encrypted_payload}')
            except Exception as e:
                self.error_occurred.emit(f'Falha ao criptografar/enviar mensagem: {e}')
        else:
            self.system_message.emit('Chave AES ainda não estabelecida. Aguarde o handshake.')

    def send_message(self, message):
        if self.running:
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.message_queue.put(message))
                loop.close()
            except Exception:
                try:
                    asyncio.run_coroutine_threadsafe(
                        self.message_queue.put(message), asyncio.get_event_loop()
                    )
                except Exception as e:
                    self.error_occurred.emit(f'Erro ao enfileirar mensagem: {str(e)}')

    def stop(self):
        self.running = False
        self.quit()
        self.wait()


class ChatWindow(QWidget):

    def __init__(self, username=None, recipient=None, server_address=None):
        super().__init__()

        self.username = username
        self.recipient = recipient
        self.server_address = server_address

        self.setWindowTitle(f'Confy - Chat com {self.recipient}')

        self.setup_ui()

        self.websocket_thread = None
        self.connection_status = 'Desconectado'

        if all([username, recipient, server_address]):
            self.connect_to_server()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)

        self.messages_area = QTextEdit()
        self.messages_area.setReadOnly(True)
        self.messages_area.setStyleSheet(
            """
            QTextEdit {
                border: 1.3px solid #393939;
                border-radius: 10px;
                color: white;
                padding: 8px;
                background-color: #202020;
            }
            """
        )
        layout.addWidget(self.messages_area)

        send_layout = QHBoxLayout()

        self.message_input = QLineEdit(placeholderText='Mensagem')
        self.message_input.setFixedHeight(40)
        self.message_input.setStyleSheet(
            """
            QLineEdit {
                border: 1.3px solid #393939;
                border-radius: 10px;
                color: white;
                padding: 8px;
                background-color: #303030;
            }
            """
        )
        self.message_input.returnPressed.connect(self.send_message)

        self.send_button = QPushButton('Enviar')
        self.send_button.setFixedSize(60, 40)
        self.send_button.setStyleSheet(
            """
            QPushButton {
                background-color: white;
                color: black;
                border-radius: 10px;
            }
            
            QPushButton:hover {
                background-color: #C0C0C0;
            }
            
            QPushButton:disabled {
                background-color: #666666;
                color: #999999;
            }
            """
        )
        self.send_button.clicked.connect(self.send_message)

        send_layout.addWidget(self.message_input)
        send_layout.addWidget(self.send_button)

        layout.addLayout(send_layout)
        self.setLayout(layout)

        self.update_connection_status('Desconectado')

    def connect_to_server(self):
        if self.websocket_thread and self.websocket_thread.isRunning():
            return

        self.websocket_thread = WebSocketThread(self.server_address, self.username, self.recipient)

        self.websocket_thread.message_received.connect(self.on_message_received)
        self.websocket_thread.connection_status.connect(self.on_connection_status)
        self.websocket_thread.system_message.connect(self.on_system_message)
        self.websocket_thread.error_occurred.connect(self.on_error_occurred)

        self.websocket_thread.start()

    def send_message(self):
        message = self.message_input.text().strip()
        if not message:
            return

        if not self.websocket_thread or not self.websocket_thread.isRunning():
            self.show_error('Não conectado ao servidor')
            return

        self.add_message_to_chat('Você', message, is_own=True)

        self.websocket_thread.send_message(message)

        self.message_input.clear()

    def on_message_received(self, sender, message):
        self.add_message_to_chat(sender, message, is_own=False)

    def on_connection_status(self, status):
        self.update_connection_status(status)

    def on_system_message(self, message):
        self.add_system_message(message)

    def on_error_occurred(self, error):
        self.show_error(error)

    def add_message_to_chat(self, sender, message, is_own=False):
        if is_own:
            formatted_message = (
                f'<div style="color: #4CAF50; font-weight: bold;">'
                f'{sender}: '
                f'<span style="color: white; font-weight: normal;">{message}</span>'
                f'</div>'
            )
        else:
            formatted_message = (
                f'<div style="color: #2196F3; font-weight: bold;">'
                f'{sender}: '
                f'<span style="color: white; font-weight: normal;">{message}</span>'
                f'</div>'
            )

        self.messages_area.append(formatted_message)

    def add_system_message(self, message):
        formatted_message = (
            f'<div style="color: #FFC107; font-style: italic;">Sistema: {message}</div>'
        )
        self.messages_area.append(formatted_message)

    def update_connection_status(self, status):
        self.connection_status = status

        if status == 'Conectado':
            self.send_button.setEnabled(True)
            self.message_input.setEnabled(True)
            self.add_system_message('Conectado ao servidor')
        else:
            self.send_button.setEnabled(False)
            if status != 'Desconectado':
                self.add_system_message(f'Status: {status}')

    def show_error(self, error):
        self.add_system_message(f'Erro: {error}')

    def closeEvent(self, event):
        if self.websocket_thread and self.websocket_thread.isRunning():
            self.websocket_thread.stop()

        event.accept()