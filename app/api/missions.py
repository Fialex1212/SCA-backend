from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from models.schemas import MissionOut, MissionCreate, MissionAssignCat, MissionUpdate
from app.deps import get_db
from app.services import missions_service
from typing import List
from fastapi import Body

router = APIRouter()


@router.post("/missions/create/", response_model=MissionOut)
async def create_mission(mission: MissionCreate, db: Session = Depends(get_db)):
    return await missions_service.create_mission(db, mission)


@router.get("/missions/{mission_id}", response_model=MissionOut)
async def read_mission(mission_id: str, db: Session = Depends(get_db)):
    return await missions_service.get_mission(db, mission_id)


@router.get("/missions/list/", response_model=List[MissionOut])
async def list_missions(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db),
):
    return await missions_service.get_all_missions(db, skip=skip, limit=limit)


@router.put("/missions/{mission_id}", response_model=MissionOut)
async def update_mission(
    mission_id: str,
    mission_update: MissionUpdate = Body(...),
    db: Session = Depends(get_db),
):
    return await missions_service.update_mission(db, mission_id, mission_update)


@router.delete("/missions/{mission_id}", response_model=MissionOut)
async def delete_mission(mission_id: str, db: Session = Depends(get_db)):
    return await missions_service.delete_mission(db, mission_id)


@router.patch("/missions/{mission_id}/assign-cat", response_model=MissionOut)
async def assign_cat_to_mission(
    mission_id: str,
    data: MissionAssignCat,
    db: Session = Depends(get_db)
):
    return await missions_service.assign_cat_to_mission(db, mission_id, data)
