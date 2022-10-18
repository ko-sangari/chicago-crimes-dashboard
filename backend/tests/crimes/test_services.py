import pytest

from src.crimes.services import crime_services


@pytest.mark.asyncio
async def test_query_primary_types() -> None:
    primary_types = await crime_services.query_primary_types()
    assert type(primary_types) == list


@pytest.mark.asyncio
async def test_crimes() -> None:
    crimes = await crime_services.query_chicago_crimes('2022-10-01', 'THEFT')
    assert type(crimes) == list
