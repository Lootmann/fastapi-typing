from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def test_index():
    return {"hello": "world"}


@router.get("/problems")
def all_problems():
    return {"problems": "all :^)"}


@router.get("/problems/{problem_id}")
def all_problems(problem_id: int):
    return {"problem_id": problem_id}
