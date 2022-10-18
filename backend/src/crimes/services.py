import os
import json

from google.cloud import bigquery
from typing import List

from src.main import logger

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.environ.get('GOOGLE_CREDENTIALS')


class BiqQueryService:
	"""
	Class for handle bigquery Client and custom Queries.
	"""

	def __init__(self):
		self.client = bigquery.Client()

	async def query_primary_types(self) -> List[str]:
		"""
		Query for retrieving all primary_types.
		"""
		logger.debug('[Function]: query_primary_types()')

		QUERY = (
			"SELECT TO_JSON_STRING(t) AS detail FROM "
			f"(SELECT DISTINCT primary_type FROM `{os.environ.get('GOOGLE_DATASET')}`) AS t;"
		)

		query_job = self.client.query(QUERY)
		result = query_job.result()

		json_list = []
		for row in result:
			json_row = json.loads(row.detail)
			json_list.append(json_row['primary_type'])

		return sorted(json_list)


	async def query_chicago_crimes(self, date: str, primary_type: str) -> List[dict]:
		"""
		Query for retrieving all crimes based on `date` and `primary_type`.
		"""
		logger.debug('[Function]: query_chicago_crimes()')

		QUERY = (
			f"SELECT TO_JSON_STRING(t) AS detail FROM (SELECT * FROM `{os.environ.get('GOOGLE_DATASET')}` "
			f"WHERE CAST(date as DATE) = ('{date}') AND "
			f"CAST(primary_type as STRING) = ('{primary_type}')) AS t"
		)

		query_job = self.client.query(QUERY)
		result = query_job.result()

		json_list = []
		for row in result:
			json_row = json.loads(row.detail)
			if not json_row['location']:
				continue

			json_row['date'] = json_row['date'].replace('T', ' ').replace('Z', '')
			json_row['updated_on'] = json_row['updated_on'].replace('T', ' ').replace('Z', '')
			json_list.append(json_row)

		return json_list


crime_services = BiqQueryService()
