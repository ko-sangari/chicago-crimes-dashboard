from fastapi.testclient import TestClient


def test_primary_types(client: TestClient) -> None:
    response = client.get("/crimes/primary_types")

    assert response.status_code == 200 
    assert type(response.json()) == list


def test_crimes_with_params(client: TestClient) -> None:
    response = client.get("/crimes?date=2022-10-01&primary_type=THEFT")

    assert response.status_code == 200 
    assert type(response.json()) == list


def test_crimes_without_params(client: TestClient) -> None:
    response = client.get("/crimes")

    assert response.status_code == 400 
    assert type(response.json()) == dict
