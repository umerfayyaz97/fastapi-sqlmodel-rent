from sqlmodel import Field, SQLModel, create_engine
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
# from .settings import DATABASE_URL
from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# print(DATABASE_URL)

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

class Rent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    rent: int | None = None
    month: str
    status: str
    remarks: str | None = None


# connection_string = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg")
# print(connection_string)

engine = create_engine(DATABASE_URL, echo=True) # type: ignore

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()   
print(engine)


