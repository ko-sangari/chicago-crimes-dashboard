import logging

from fastapi import FastAPI
from dotenv import load_dotenv

from src.redis import redis_cache

load_dotenv()
app = FastAPI()
redis = redis_cache
logger = logging.getLogger("uvicorn.error")

from src.crimes import routes as crime_routes
app.include_router(crime_routes.router, prefix="/crimes", tags=["crimes"])


@app.on_event('startup')
async def startup_event() -> None:
	"""
	Function that should be run before the application starts.
	"""
	await redis.init_cache()
	await redis.flushdb()


@app.on_event('shutdown')
async def shutdown_event() -> None:
	"""
	Function that should be run when the application is shutting down.
	"""
	await redis.close()
