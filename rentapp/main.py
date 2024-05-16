# from sqlmodel import Field, Session,  SQLModel, create_engine, col, or_
# from sqlmodel import select
# from contextlib import asynccontextmanager
# from typing import Union, Optional, Annotated
# # from .settings import DATABASE_URL
# from dotenv import load_dotenv
# import os


# # load environment variables from .env file
# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")

# # SQLITE_URL = os.getenv("SQLITE_URL")
# # print(DATABASE_URL)


# #class HERO with row attributes
# class Hero(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     secret_name: str
#     age: int | None = None

# class Rent(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     description: str
#     rent: int | None = None
#     month: str
#     status: str
#     remarks: str | None = None


# # connection_string = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg")
# # print(connection_string)

# engine = create_engine(DATABASE_URL) # type: ignore

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# # def create_heroes():
# #     hero1 = Hero(name="ShapatarMAN" , secret_name="SHP")
# #     hero2 = Hero(name="ShapatarMAN2", secret_name="SHP2")
# #     hero3 = Hero(name="ShapatarMAN3", secret_name="SHP3")

# #     with Session(engine) as session:
# #         session.add(hero1)
# #         session.add(hero2)
# #         session.add(hero3)

# #         session.commit()




# # def add_rent_details():
# #     rent1 = Rent(description="Muzaffar Market", rent=9500, month="April 2024", status="received", remarks="Rent increased yearly" )
# #     rent2 = Rent(description="Ramzan City", rent=10000, month="April 2024", status="not received")
# #     rent3 = Rent(description="Ramzan Town", rent=10000, month="April 2024", status="Previous month due also")

# #     with Session(engine) as session:
# #         session.add(rent1)
# #         session.add(rent2)
# #         session.add(rent3)

# #         session.commit()

# #getting data from tables
# # def get_data():
# #     with Session(engine) as session:

#         # HERO DB

#         #(select) returns iterable object
#         # statement = select(Hero)

#         # results = session.exec(statement)

#         #(.all) returns List instead of object
#         # heroes = results.all()
#         # print(heroes)

#         # statement = select(Hero).where(Hero.id == 1)
#         # results = session.exec(statement)
#         # heroes = session.exec(select(Hero).where(Hero.name == 'ShapatarMAN')).first()
#         # heroes = session.get(Hero, 46)
#         # print('Hero: ',heroes)
#         # for hero in results:
#         #     print(hero)

#         # heroes = session.exec(select(Hero)).all()
#         # print(heroes)

#         # ------------------------------------------------  

#         # RENT DB

#         # statement = select(Rent).where(Rent.description == "Muzaffar Market", col(Rent.rent) >= 10000)
#         # results = session.exec(statement)
#         # for rent in results:
#         #     print(rent)

#         # rent = session.exec(select(Rent)).all()
#         # print(rent)

# # deleting rows
# def delete_rent():
#     with Session(engine) as session:
#         statement = select(Rent).where(Rent.description == "Muzaffar Market")
#         results = session.exec(statement)
#         for rent in results:
#             print(rent)
#             session.delete(rent)
#         session.commit()

#         statement = select(Rent).where(Rent.description == "Muzaffar Market")
#         results = session.exec(statement)
#         rent = results.first()

#         if rent is None:
#             print("There is no description avsailable as 'Muzaffar Market' ")

        

# # def update_heroes():
# #     with Session(engine) as session:
# #         statement = select(Hero).where(Hero.name == 'ShapatarMAN')
# #         heroes = session.exec(statement)
# #         for hero in heroes:
# #             print(hero)
# #             hero.age = 92
# #             session.add(hero)
        
# #         session.commit()
#         # for hero in heroes:
#         #     session.refresh(hero)
#             # print(hero)

#         # update_heroes = session.exec(statement)

#         # print('updated hero=' )
#         # for hero in update_heroes:
#         #     print(hero)


# def main():
#     create_db_and_tables()
#     # create_heroes()
#     # add_rent_details()
#     # get_data()
#     # update_heroes()
#     delete_rent()

# # Run if called main file, if imported does not call
# if __name__ == "__main__":
#     main()   
# # print(engine)

