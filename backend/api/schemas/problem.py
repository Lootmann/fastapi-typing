from pydantic import BaseModel, Field


class ProblemBase(BaseModel):
    sentence: str = Field("", example="typing sentence")


class ProblemCreate(ProblemBase):
    pass


class ProblemCreateResponse(ProblemCreate):
    id: int

    class Config:
        orm_mode = True


class Problem(ProblemBase):
    id: int

    class Config:
        orm_mode = True
