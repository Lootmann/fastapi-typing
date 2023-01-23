from fastapi import APIRouter

router = APIRouter()


@router.get("/records")
def all_records():
    return {"records": "all :^)"}


@router.get("/records/{record_id}")
def all_records(record_id: int):
    return {"record_id": record_id}


@router.post("/records")
def create_record():
    return {"msg": "create a record"}


@router.delete("/records/{record_id}")
def delete_record(record_id: int):
    return {"delete": record_id}
