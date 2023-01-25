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
