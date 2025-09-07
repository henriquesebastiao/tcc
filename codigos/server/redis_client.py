import redis.asyncio as redis

from server.settings import get_settings

settings = get_settings()

redis_client = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True
)
