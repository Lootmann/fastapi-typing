from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_all_problems():
    response = client.get("/problems")
    assert response.status_code == 200
    assert response.json() == {"problems": "all :^)"}


def test_problem():
    response = client.get("/problems/1")
    assert response.status_code == 200
    assert response.json() == {"problem_id": 1}
