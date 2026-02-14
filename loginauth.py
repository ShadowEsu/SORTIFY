from sqlmodel import SQLModel, Field
from typing import Optional
from contextlib import asynccontextmanager

class Item(SQModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    
from sqlmodel import create_engine, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
from fastapi import FastAPI

app = FastAPI()

@asynccontextmanager
async def get_session(app: FastAPI):
    with Session(engine) as session:
        yield session
        
from fastapi import Depends

@app.post("/items/")
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
from typing import list
from sqlmodel import select
@app.get("/items/", response_model=list[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
