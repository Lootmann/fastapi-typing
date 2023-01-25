from typing import List

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.record as record_model
import api.schemas.record as record_scheme


async def get_all_records(db: AsyncSession) -> List[record_model.Record]:
    result: Result = await (
        db.execute(
            select(
                record_model.Record.id,
                record_model.Record.actual_typing,
                record_model.Record.duration,
                record_model.Record.registered_at,
            )
        )
    )
    return result.all()  # type: ignore


async def get_record(db: AsyncSession, record_id: int) -> record_model.Record | None:
    result: Result = await db.execute(
        select(record_model.Record).filter(record_model.Record.id == record_id)
    )

    record: record_model.Record | None = result.first()

    return record[0] if record else None


async def create_record(
    db: AsyncSession, record_create: record_scheme.RecordCreate
) -> record_model.Record:
    record = record_model.Record(**record_create.dict())
    db.add(record)

    await db.commit()
    await db.refresh(record)

    return record


async def delete_record(db: AsyncSession, original: record_model.Record):
    await db.delete(original)
    await db.commit()
