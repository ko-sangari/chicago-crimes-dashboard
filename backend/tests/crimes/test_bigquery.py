import os
import json
import pytest

from google.cloud import bigquery
from google.auth.exceptions import DefaultCredentialsError


def test_bigquery_credentials() -> None:
    try:
        bigquery.Client()
    except Exception as exception:
        pytest.fail(str(exception))


def test_bigquery_has_column_location() -> None:
    _date = '2022-10-01'
    _primary_type = 'THEFT'
    QUERY = (
        f"SELECT TO_JSON_STRING(t) AS detail FROM (SELECT * FROM `{os.environ.get('GOOGLE_DATASET')}` "
        f"WHERE CAST(date as DATE) = ('{_date}') AND "
        f"CAST(primary_type as STRING) = ('{_primary_type}') LIMIT 1) AS t"
    )

    client = bigquery.Client()
    query_job = client.query(QUERY)
    result = query_job.result()

    for row in result:
        first_row = row
    json_first_row = json.loads(first_row.detail)
    
    assert ('location' in json_first_row) == True


def test_fail_bigquery_credentials(without_bigquery_credential) -> None:
    with pytest.raises(DefaultCredentialsError):
        bigquery.Client()
