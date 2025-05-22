from sqlalchemy.orm import Session
from models.schemas import MissionCreate, MissionAssignCat, MissionUpdate
from db import crud
from models.models import Mission


async def create_mission(db: Session, mission_data: MissionCreate) -> Mission:
    return crud.create_mission(db, mission_data)


async def get_mission(db: Session, mission_id: str) -> Mission:
    print(mission_id)
    return crud.get_mission(db, mission_id)


async def get_all_missions(
    db: Session, skip: int = 0, limit: int = 10
) -> list[Mission]:
    return crud.get_list_missions(db, skip=skip, limit=limit)


async def update_mission(db: Session, mission_id: str, mission_update: MissionUpdate) -> Mission:
    return crud.update_mission(db, mission_id, mission_update)



async def delete_mission(db: Session, mission_id: str) -> Mission:
    return crud.delete_mission(db, mission_id)


async def assign_cat_to_mission(
    db: Session, mission_id: str, data: MissionAssignCat
) -> Mission:
    return crud.assign_cat_to_mission(db, mission_id, data.cat_id)
