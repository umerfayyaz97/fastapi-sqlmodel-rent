from sqlmodel import Field, Session,  SQLModel, create_engine, col, or_
from sqlmodel import select
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

class Rent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    rent_amount: int | None = None
    month: str = Field(index=True)
    year: str = Field(index=True)
    status: str
    location_id: int | None = Field(foreign_key="location.id")


# class Rent(SQLModel, table=True):
#   id: Optional[int] = Field(default=None, primary_key=True)
#   rent_amount: Optional[int] = None
#   month: str = Field(index=True)
#   year: str = Field(index=True)
#   status: str
#   location_id: Optional[int] = Field(foreign_key="location.id")

class Location(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    location_name: str = Field(index=True)
    total_rent: int | None = None

engine = create_engine(DATABASE_URL) # type: ignore

# print(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def main():        
    create_db_and_tables()
    
# Run if called main file, if imported does not call
if __name__ == "__main__":
    main()   