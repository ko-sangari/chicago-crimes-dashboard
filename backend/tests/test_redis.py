import json
import pytest
from aioredis import Redis


@pytest.mark.asyncio
async def test_redis_cach_success(redis: Redis) -> None:
    _key = 'tets_key'
    _value = json.dumps({'test': 'OK'})

    await redis.set(_key, _value)
    cached = await redis.get(_key)

    assert cached == _value


@pytest.mark.asyncio
async def test_redis_cach_fail(redis: Redis) -> None:
    _key = 'tets_key'
    _value = json.dumps({'test': 'OK'})

    cached = await redis.get(_key)

    assert cached == None
