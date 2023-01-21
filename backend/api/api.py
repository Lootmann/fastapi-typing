from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def test_index():
    return {"hello": "world"}
