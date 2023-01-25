from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from api.db import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True)
    sentence = Column(String(1024))
