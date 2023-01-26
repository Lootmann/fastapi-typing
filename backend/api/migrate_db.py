from sqlalchemy import create_engine

from api.models.problem import Base as problem_base
from api.models.record import Base as record_base

DB_URL = "sqlite:///db.sqlite3"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    problem_base.metadata.drop_all(bind=engine)
    problem_base.metadata.create_all(bind=engine)
    record_base.metadata.drop_all(bind=engine)
    record_base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
