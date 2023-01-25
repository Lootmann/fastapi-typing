from typing import List, Tuple

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


async def get_all_problems(db: AsyncSession) -> List[Tuple[int, str]]:
    result: Result = await (
        db.execute(
            select(
                problem_model.Problem.id,
                problem_model.Problem.sentence,
            )
        )
    )
    return result.all()  # type: ignore


async def get_problem(db: AsyncSession, problem_id: int) -> Tuple[int, str] | None:
    result: Result = await db.execute(
        select(problem_model.Problem).filter(problem_model.Problem.id == problem_id)
    )

    problem: Tuple[problem_model.Problem] | None = result.first()  # type: ignore

    if problem is None:
        return None

    return problem[0]
