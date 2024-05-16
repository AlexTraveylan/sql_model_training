import contextlib
from typing import Optional

from pydantic import ConfigDict, PositiveInt
from sqlalchemy import create_engine
from sqlmodel import Field, Session, SQLModel

from app.adapter.exception.app_exception import AppException


class BaseSQLModel(SQLModel):
    model_config = ConfigDict(validate_assignment=True)


class Personage(BaseSQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=20, min_length=2)
    age: PositiveInt


class Animal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=20, min_length=2)


engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


@contextlib.contextmanager
def unit():
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise AppException(f"Rolling back, cause : {str(e)}") from e
    finally:
        session.close()
