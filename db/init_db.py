from db.session import engine, Base
from models.models import Cat
from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating a tabels...")
    Base.metadata.create_all(bind=engine)
    print("Tables created")
    
    yield