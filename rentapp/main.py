from sqlmodel import Field, SQLModel, create_engine

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


