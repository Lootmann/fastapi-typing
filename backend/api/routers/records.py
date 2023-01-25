from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.record as record_crud
import api.schemas.record as record_schema
from api.db import get_db

router = APIRouter()


@router.get("/records", response_model=List[record_schema.Record])
async def all_records(db: AsyncSession = Depends(get_db)):
    return await record_crud.get_all_records(db)


@router.get("/records/{record_id}")
async def all_records(record_id: int, db: AsyncSession = Depends(get_db)):
    return await record_crud.get_record(db, record_id)


@router.post("/records", response_model=record_schema.RecordCreateResponse)
async def create_record(
    record_body: record_schema.RecordCreate, db: AsyncSession = Depends(get_db)
):
    return await record_crud.create_record(db, record_body)


@router.delete("/records/{record_id}", response_model=None)
async def delete_record(record_id: int, db: AsyncSession = Depends(get_db)):
    record = await record_crud.get_record(db, record_id=record_id)

    if not record:
        raise HTTPException(status_code=404, detail="Record Not Found :^)")

    return await record_crud.delete_record(db, record)
