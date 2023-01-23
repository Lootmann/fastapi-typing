from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_all_records():
    response = client.get("/records")
    assert response.status_code == 200
    assert response.json() == {"records": "all :^)"}


def test_record_by_id():
    response = client.get("/records/1")
    assert response.status_code == 200
    assert response.json() == {"record_id": 1}


def test_post_record():
    response = client.post("/records")
    assert response.status_code == 200


def test_delete_record():
    response = client.delete("/records/1")
    assert response.status_code == 200
