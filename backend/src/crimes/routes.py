from fastapi import BackgroundTasks, APIRouter, status, HTTPException

from typing import List

from src.main import redis, logger
from src.crimes.services import crime_services

router = APIRouter()


@router.get("/primary_types")
async def retrieve_primary_types(background_tasks: BackgroundTasks) -> List:
	"""
	Retrieves all crime's primary types as a List to use in Dashboard Filter.
		1st, Check Redis for same `primary_type` list.
		2nd, Call the related function from Services.
	"""
	data = await redis.get('primary_type')

	if not data:
		logger.debug('Retrieve Data from BigQuery.')
		data = await crime_services.query_primary_types()
		background_tasks.add_task(redis.set, 'primary_type', data)

	return data


@router.get("")
async def retrieve_crimes(background_tasks: BackgroundTasks, date: str = None, primary_type: str = None) -> List[dict]:
	"""
	Retrieves crimes details based on the `date` and `primary_type`.
		1st, Validation for both URL quety params.
		2nd, Check Redis for same requested report.
		3rd, Call the related function from Services.
	"""
	if not all([date, primary_type]):
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail={
				'message': 'Both `date` and `primary_type` should be send as query params.'
			},
		)

	data = await redis.get(f"{date}:{primary_type}")

	if not data:
		logger.debug('Retrieve Data from BigQuery.')
		data = await crime_services.query_chicago_crimes(date, primary_type)
		background_tasks.add_task(redis.set, f"{date}:{primary_type}", data)

	return data
