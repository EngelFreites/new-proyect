from typing import Annotated
from fastapi import FastAPI
from sqlmodel import create_engine, Session, SQLModel
from fastapi import Depends

sqlite_name = "db.sqlite3"
engine = create_engine(f"sqlite:///{sqlite_name}")


def create_db_and_tables(app:FastAPI):
  SQLModel.metadata.create_all(engine)
  yield
  
def get_session():
  with Session(engine) as session:
    yield session

  
SessionDep = Annotated[Session, Depends(get_session)]