from typing import List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.problem as problem_crud
import api.schemas.problem as problem_schema
from api.db import get_db

router = APIRouter()


@router.get("/problems", response_model=List[problem_schema.Problem])
async def all_problems(db: AsyncSession = Depends(get_db)):
    return await problem_crud.get_all_problems(db)


@router.get("/problems/{problem_id}")
async def problems_by_id(problem_id: int, db: AsyncSession = Depends(get_db)):
    return await problem_crud.get_problem(db, problem_id)


@router.post("/problems", response_model=problem_schema.ProblemCreateResponse)
async def create_problem(
    problem_body: problem_schema.ProblemCreate, db: AsyncSession = Depends(get_db)
):
    return await problem_crud.create_problem(db, problem_body)


@router.put("/problems/{problem_id}", response_model=problem_schema.ProblemCreateResponse)
async def update_problem(
    problem_id: int, problem_body: problem_schema.ProblemCreate, db: AsyncSession = Depends(get_db)
):
    problem = await problem_crud.get_problem(db, problem_id=problem_id)

    if not problem:
        raise HTTPException(status_code=404, detail="Problem Not Found :^)")

    return await problem_crud.update_problem(db, problem_body, updated=problem)


@router.delete("/problems/{problem_id}", response_model=None)
async def delete_problem(problem_id: int, db: AsyncSession = Depends(get_db)):
    problem = await problem_crud.get_problem(db, problem_id=problem_id)

    if not problem:
        raise HTTPException(status_code=404, detail="Problem Not Found :^)")

    return await problem_crud.delete_problem(db, problem)
