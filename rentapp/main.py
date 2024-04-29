from sqlmodel import Field, Session,  SQLModel, create_engine, col, or_
from sqlmodel import select
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
# from .settings import DATABASE_URL
from dotenv import load_dotenv
import os


# load environment variables from .env file
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLITE_URL = os.getenv("SQLITE_URL")
# print(DATABASE_URL)


#class HERO with row attributes
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

# def create_heroes():
#     hero1 = Hero(name="ShapatarMAN" , secret_name="SHP")
#     hero2 = Hero(name="ShapatarMAN2", secret_name="SHP2")
#     hero3 = Hero(name="ShapatarMAN3", secret_name="SHP3")

#     with Session(engine) as session:
#         session.add(hero1)
#         session.add(hero2)
#         session.add(hero3)

#         session.commit()




# def add_rent_details():
#     rent1 = Rent(description="Muzaffar Market", rent=9500, month="April 2024", status="received", remarks="Rent increased yearly" )
#     rent2 = Rent(description="Ramzan City", rent=10000, month="April 2024", status="not received")
#     rent3 = Rent(description="Ramzan Town", rent=10000, month="April 2024", status="Previous month due also")

#     with Session(engine) as session:
#         session.add(rent1)
#         session.add(rent2)
#         session.add(rent3)

#         session.commit()

#getting data from tables
def get_data():
    with Session(engine) as session:

        # HERO DB

        # statement = select(Hero)
        # results = session.exec(statement)
        # heroes = results.all()
        # print(heroes)

        # statement = select(Hero).where(Hero.id == 3 ).where(Hero.secret_name == "SHP2")
        # results = session.exec(statement)
        # for hero in results:
        #     print(hero)

        # heroes = session.exec(select(Hero)).all()
        # print(heroes)

        # ------------------------------------------------  

        # RENT DB

        statement = select(Rent).where(Rent.description == "Muzaffar Market", col(Rent.rent) >= 10000)
        results = session.exec(statement)
        for rent in results:
            print(rent)

        # rent = session.exec(select(Rent)).all()
        # print(rent)

def main():
    create_db_and_tables()
    # create_heroes()
    # add_rent_details()
    get_data()

# Run if called main file, if imported does not call
if __name__ == "__main__":
    main()   
# print(engine)

