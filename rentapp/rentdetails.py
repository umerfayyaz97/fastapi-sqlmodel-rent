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

class Location(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    location_name: str = Field(index=True)
    total_rent: int | None = None

engine = create_engine(str(DATABASE_URL)) 

#creating Location Tables

def rent_location():
    with Session(engine) as session:
        daska = Location(location_name="Ramzan Town 3.5", total_rent = 18000)
        lahore = Location(location_name="Lahore", total_rent = 45000)
        muzaffar_shop = Location(location_name="Muzaffar Shop")

        session.add(daska, lahore, muzaffar_shop)
        session.commit()


# print(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def main():        
    create_db_and_tables()
    rent_location()
    
# Run if called main file, if imported does not call
if __name__ == "__main__":
    main()   