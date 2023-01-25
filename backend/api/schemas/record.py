from datetime import datetime

from pydantic import BaseModel, Field


class RecordBase(BaseModel):
    actual_typing: str = Field("", example="actual typing sentence")
    duration: int = Field(0, example="a time to required typing")
    registered_at: datetime = Field(datetime.now(), example="when typing")


class RecordCreate(RecordBase):
    pass


class RecordCreateResponse(RecordCreate):
    id: int

    class Config:
        orm_mode = True


class Record(RecordBase):
    id: int

    class Config:
        orm_mode = True
