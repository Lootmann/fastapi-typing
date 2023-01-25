from typing import List

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.problem as problem_model
import api.schemas.problem as problem_schema


async def create_problem(
    db: AsyncSession, problem_create: problem_schema.ProblemCreate
) -> problem_model.Problem:
    problem = problem_model.Problem(**problem_create.dict())
    db.add(problem)

    await db.commit()
    await db.refresh(problem)

    return problem


async def get_all_problems(db: AsyncSession) -> List[problem_model.Problem]:
    result: Result = await (
        db.execute(
            select(
                problem_model.Problem.id,
                problem_model.Problem.sentence,
            )
        )
    )
    return result.all()  # type: ignore


async def get_problem(db: AsyncSession, problem_id: int) -> problem_model.Problem | None:
    result: Result = await db.execute(
        select(problem_model.Problem).filter(problem_model.Problem.id == problem_id)
    )

    problem: problem_model.Problem | None = result.first()  # type: ignore

    if problem is None:
        return None

    return problem[0]


async def update_problem(
    db: AsyncSession,
    problem_create: problem_schema.ProblemCreate,
    updated: problem_model.Problem,
) -> problem_model.Problem:
    updated.sentence = problem_create.sentence  # type:ignore
    db.add(updated)

    await db.commit()
    await db.refresh(updated)
    return updated


async def delete_problem(db: AsyncSession, original: problem_model.Problem):
    await db.delete(original)
    await db.commit()
