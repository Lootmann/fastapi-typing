from fastapi import APIRouter

router = APIRouter()


@router.get("/problems")
def all_problems():
    return [
        {"id": 1, "sentence": "very first"},
        {"id": 2, "sentence": "whe hello friends :^)"},
    ]


@router.get("/problems/{problem_id}")
def problems_by_id(problem_id: int):
    return {"problem_id": problem_id}
