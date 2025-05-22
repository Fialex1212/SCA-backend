from sqlalchemy.orm import Session
from models.schemas import CatCreate, CatUpdate
from db import crud
from app.utils.cat_validator import validate_breed
from models.models import Cat


async def create_cat_service(db: Session, cat_data: CatCreate) -> Cat:
    await validate_breed(cat_data.breed)
    return crud.create_cat(db, cat_data)


async def get_cat(db: Session, cat_id: str) -> Cat:
    print(cat_id)
    return crud.get_cat(db, cat_id)


async def get_all_cats(db: Session, skip: int = 0, limit: int = 10) -> list[Cat]:
    return crud.get_list_cat(db, skip=skip, limit=limit)


async def update_cat(db: Session, cat_id: str, cat_update_data: CatUpdate) -> Cat:
    return crud.update_cat(db, cat_id, cat_update_data)


async def delete_cat(db: Session, cat_id: str) -> Cat:
    return crud.delete_cat(db, cat_id)
