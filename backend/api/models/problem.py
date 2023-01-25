from sqlalchemy import Column, Integer, String, DateTime

from api.db import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True)
    sentence = Column(String(1024))


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    actual_typing = Column(String(9999))
    duration = Column(Integer)
    registered_at = Column(DateTime)
