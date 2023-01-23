from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_all_problems():
    response = client.get("/problems")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "sentence": "very first"},
        {"id": 2, "sentence": "whe hello friends :^)"},
    ]


def test_problem_by_id():
    response = client.get("/problems/1")
    assert response.status_code == 200
    assert response.json() == {"problem_by_id": 1}


def test_post_problem():
    response = client.post("/problems")
    assert response.status_code == 200


def test_put_problem():
    response = client.put("/problems")
    assert response.status_code == 405


def test_delete_problem():
    response = client.delete("/problems/1")
    assert response.status_code == 200
