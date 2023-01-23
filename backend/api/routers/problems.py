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
    return {"problem_by_id": problem_id}


@router.post("/problems")
def create_problem():
    return {"create": "create a problem"}


@router.put("/problems/{problem_id}")
def update_problem(problem_id: int):
    return {"update": problem_id}


@router.delete("/problems/{problem_id}")
def delete_problem(problem_id: int):
    return {"delete": problem_id}
