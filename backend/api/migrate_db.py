from sqlalchemy import create_engine

from api.models.problem import Base


DB_URL = "sqlite:///db.sqlite3"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
