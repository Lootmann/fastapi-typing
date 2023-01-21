from fastapi import APIRouter

router = APIRouter()


@router.get("/records")
def all_records():
    return {"records": "all :^)"}


@router.get("/records/{record_id}")
def all_records(record_id: int):
    return {"record_id": record_id}
