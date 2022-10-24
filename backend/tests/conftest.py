import os
import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from aioredis import from_url
from typing import Generator

from src.main import app, redis


@pytest.fixture(scope="module")
def client() -> Generator:
	"""
	Create a FastAPI TestClient which includes `redis` dependency.
	"""

	def _get_redis_client():
		yield from_url(os.environ.get('REDIS_SERVER'),  decode_responses=True)

	app.dependency_overrides[redis] = _get_redis_client
	with TestClient(app) as client:
		yield client


@pytest_asyncio.fixture(scope="function")
async def redis() -> Generator:
	"""
	Create a `redis` instance.
	"""
	redis = from_url(os.environ.get('REDIS_SERVER'),  decode_responses=True)
	await redis.flushdb()
	yield redis


@pytest.fixture
def without_bigquery_credential() -> None:
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''
