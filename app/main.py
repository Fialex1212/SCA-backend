from fastapi import FastAPI
from app.cors import add_cors
from db.init_db import lifespan
from app.api import cats, missions

app = FastAPI(lifespan=lifespan)
add_cors(app)


@app.get("/ping")
async def ping():
    return {"message": "pong"}


app.include_router(cats.router, tags=["Cats"])
app.include_router(missions.router, tags=["Missions"])


