from typing import List

from fastapi import APIRouter

import api.schemas.problem as problem_schema

router = APIRouter()


@router.get("/problems", response_model=List[problem_schema.Problem])
def all_problems():
    return [
        problem_schema.Problem(id=1, sentence="very first"),
        problem_schema.Problem(id=2, sentence="why hello friends :^)"),
    ]


@router.get("/problems/{problem_id}")
def problems_by_id(problem_id: int):
    return {"problem_by_id": problem_id}


@router.post("/problems", response_model=problem_schema.ProblemCreateResponse)
def create_problem(problem_body: problem_schema.ProblemCreate):
    return problem_schema.ProblemCreateResponse(id=1, **problem_body.dict())


@router.put("/problems/{problem_id}", response_model=problem_schema.ProblemCreateResponse)
def update_problem(problem_id: int, problem_body: problem_schema.ProblemCreate):
    return problem_schema.ProblemCreateResponse(id=problem_id, **problem_body.dict())


@router.delete("/problems/{problem_id}", response_model=None)
def delete_problem():
    return
