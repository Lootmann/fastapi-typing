from datetime import datetime

import pytest
import starlette.status

# noinspection PyUnresolvedReferences
from tests.init_async_client import async_client


@pytest.mark.asyncio
async def test_create_and_read(async_client):
    # create
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "actual_typing": "This is a super typing test.",
        "duration": 102,
        "registered_at": current_date,
    }
    resp = await async_client.post("/records", json=data)
    resp_obj = resp.json()
    assert resp.status_code == starlette.status.HTTP_200_OK
    assert resp_obj["actual_typing"] == "This is a super typing test."
    assert resp_obj["duration"] == 102
    assert resp_obj["registered_at"] == current_date.replace(" ", "T")

    # get
    resp = await async_client.get(f"/records/{resp_obj['id']}")
    resp_obj = resp.json()
    assert resp_obj["actual_typing"] == "This is a super typing test."
    assert resp_obj["duration"] == 102
    assert resp_obj["registered_at"] == current_date.replace(" ", "T")


@pytest.mark.asyncio
async def test_create_many_and_read(async_client):
    # create
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "actual_typing": "This is a super typing test.",
        "duration": 102,
        "registered_at": current_date,
    }

    await async_client.post("/records", json=data)
    await async_client.post("/records", json=data)
    await async_client.post("/records", json=data)
    resp = await async_client.post("/records", json=data)
    assert resp.status_code == starlette.status.HTTP_200_OK

    # get
    resp = await async_client.get("/records")
    resp_obj = resp.json()
    assert len(resp_obj) == 4
    assert resp_obj[-1]["actual_typing"] == "This is a super typing test."


@pytest.mark.asyncio
async def test_delete(async_client):
    # create
    data = {
        "actual_typing": "This will remove",
        "duration": 59,
        "registered_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    }

    resp = await async_client.post("/records", json=data)
    assert resp.status_code == starlette.status.HTTP_200_OK

    resp_obj = resp.json()
    record_id = resp_obj["id"]

    # get
    resp = await async_client.get(f"/records/{record_id}")
    resp_obj = resp.json()

    assert resp.status_code == starlette.status.HTTP_200_OK
    assert resp_obj["actual_typing"] == "This will remove"

    # delete
    await async_client.delete(f"/records/{record_id}")

    # get
    resp = await async_client.get(f"/records/{record_id}")
    resp_obj = resp.json()
    assert resp_obj is None

    resp = await async_client.get(f"/records")
    resp_obj = resp.json()
    assert len(resp_obj) == 0
