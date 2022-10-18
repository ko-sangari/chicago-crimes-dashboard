import os
import json
from typing import Optional, List, Any, Union

from aioredis import Redis, from_url

ONE_DAY = 86400	# Seconds


#Create a RedisCache instance
class RedisCache:

    def __init__(self):
        self.redis_cache: Optional[Redis] = None
        
    async def init_cache(self):
        self.redis_cache = from_url(os.environ.get('REDIS_SERVER'),  decode_responses=True)
    
    async def keys(self, pattern):
        return await self.redis_cache.keys(pattern)

    async def set(self, key: str, value: List):
        return await self.redis_cache.set(key, json.dumps(value), ex=ONE_DAY)
    
    async def get(self, key: str):
        cached_data = await self.redis_cache.get(key)

        if cached_data:
            return json.loads(cached_data)

    async def flushdb(self) -> None:
        await self.redis_cache.flushdb()

    async def close(self) -> None:
        await self.redis_cache.close()


redis_cache = RedisCache()
