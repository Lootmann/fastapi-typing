import pytest
import pytest_asyncio
import starlette.status
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from api.db import Base, get_db
from api.main import app

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    # Async用のengineとsessionを作成
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=async_engine,
        class_=AsyncSession,
    )

    # テスト用にオンメモリのSQLiteテーブルを初期化（関数ごとにリセット）
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # DIを使ってFastAPIのDBの向き先をテスト用DBに変更
    async def get_test_db():
        async with async_session() as session:  # type: ignore
            yield session

    app.dependency_overrides[get_db] = get_test_db

    # テスト用に非同期HTTPクライアントを返却
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


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
    assert resp.json() == None
