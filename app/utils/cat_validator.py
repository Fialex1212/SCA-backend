import httpx
from fastapi import HTTPException

async def validate_breed(breed: str):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.thecatapi.com/v1/breeds")
        if response.status_code != 200:
            raise HTTPException(status_code=503, detail="CatAPI unavailable")
        valid_breeds = [b["name"].lower() for b in response.json()]
        if breed.lower() not in valid_breeds:
            raise HTTPException(status_code=400, detail="Invalid cat breed")
