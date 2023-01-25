import pytest
import starlette.status
from httpx import AsyncClient

# noinspection PyUnresolvedReferences
from tests.init_async_client import async_client


@pytest.mark.asyncio
async def test_create_and_read(async_client: AsyncClient):
    await async_client.post("/problems", json={"sentence": "hoge"})
    await async_client.post("/problems", json={"sentence": "hage"})
    await async_client.post("/problems", json={"sentence": "hige"})
    resp = await async_client.post("/problems", json={"sentence": "テストタスク"})
    assert resp.status_code == starlette.status.HTTP_200_OK

    resp_obj = resp.json()
    assert resp_obj["sentence"] == "テストタスク"

    resp = await async_client.get("/problems")
    assert resp.status_code == starlette.status.HTTP_200_OK

    resp_obj = resp.json()
    assert len(resp_obj) == 4
    assert resp_obj[-1]["sentence"] == "テストタスク"


@pytest.mark.asyncio
async def test_create_and_update(async_client: AsyncClient):
    # create
    resp = await async_client.post("/problems", json={"sentence": "hoge"})
    assert resp.status_code == starlette.status.HTTP_200_OK

    resp_obj = resp.json()
    assert resp_obj["sentence"] == "hoge"

    # update
    problem_id = resp_obj["id"]
    resp = await async_client.put(f"/problems/{problem_id}", json={"sentence": "updated :^)"})
    assert resp.status_code == starlette.status.HTTP_200_OK

    # get
    resp_obj = resp.json()
    assert resp_obj["id"] == problem_id
    assert resp_obj["sentence"] == "updated :^)"


@pytest.mark.asyncio
async def test_delete(async_client: AsyncClient):
    # create
    resp = await async_client.post("/problems", json={"sentence": "hage"})
    assert resp.status_code == starlette.status.HTTP_200_OK

    resp_obj = resp.json()
    assert resp_obj["sentence"] == "hage"

    # get
    problem_id = resp_obj["id"]
    resp = await async_client.get(f"/problems/{problem_id}")
    assert resp.status_code == starlette.status.HTTP_200_OK
    assert resp.json()["sentence"] == "hage"

    # delete
    await async_client.delete(f"/problems/{problem_id}")

    # get
    resp = await async_client.get(f"/problems/{problem_id}")
    assert resp.status_code == starlette.status.HTTP_200_OK
    assert resp.json() is None
