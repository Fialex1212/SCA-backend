from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from models.schemas import CatOut, CatCreate, CatUpdate
from app.deps import get_db
from app.services import cats_service
from typing import List

router = APIRouter()


@router.post("/cats/create/", response_model=CatOut)
async def create_cat(cat: CatCreate, db: Session = Depends(get_db)):
    return await cats_service.create_cat_service(db, cat)


@router.get("/cats/{cat_id}", response_model=CatOut)
async def read_cat(cat_id: str, db: Session = Depends(get_db)):
    return await cats_service.get_cat(db, cat_id)


@router.get("/cats/list/", response_model=List[CatOut])
async def list_cats(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db),
):
    return await cats_service.get_all_cats(db, skip=skip, limit=limit)


@router.put("/cats/{cat_id}", response_model=CatOut)
async def update_cat(
    cat_update_data: CatUpdate, cat_id: str, db: Session = Depends(get_db)
):
    return await cats_service.update_cat(db, cat_id, cat_update_data)


@router.delete("/cats/{cat_id}", response_model=CatOut)
async def delete_cat(cat_id: str, db: Session = Depends(get_db)):
    return await cats_service.delete_cat(db, cat_id)
