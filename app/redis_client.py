import redis.asyncio as redis 
from app.config import settings

redis_pool = redis.from_url(settings.redis_url, decode_responses = True)

async def get_redis():
    return redis_pool

