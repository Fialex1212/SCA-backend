from sqlalchemy.orm import Session
from models.models import Cat, Mission, Target
from models.schemas import CatCreate, CatUpdate, MissionCreate, MissionUpdate
from fastapi import HTTPException
import uuid


def create_cat(db: Session, cat: CatCreate) -> Cat:
    db_cat = Cat(**cat.model_dump())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


def get_cat(db: Session, cat_id: str) -> Cat:
    if not cat_id:
        raise HTTPException(status_code=400, detail="cat_id must be provided")

    try:
        cat_uuid = uuid.UUID(cat_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    db_cat = db.query(Cat).filter(Cat.id == cat_uuid).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat


def get_list_cat(db: Session, skip: int = 0, limit: int = 10) -> list[Cat]:
    return db.query(Cat).offset(skip).limit(limit).all()


def update_cat(db: Session, cat_id: str, cat_update: CatUpdate) -> Cat:
    if not cat_id:
        raise HTTPException(status_code=400, detail="cat_id must be provided")

    try:
        cat_uuid = uuid.UUID(cat_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    db_cat = db.query(Cat).filter(Cat.id == cat_uuid).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="Cat not found")

    db_cat.salary = cat_update.salary
    db.commit()
    db.refresh(db_cat)
    return db_cat


def delete_cat(db: Session, cat_id: str) -> Cat:
    if not cat_id:
        raise HTTPException(status_code=400, detail="cat_id must be provided")

    try:
        cat_uuid = uuid.UUID(cat_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    db_cat = db.query(Cat).filter(Cat.id == cat_uuid).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="Cat not found")

    db.delete(db_cat)
    db.commit()
    return db_cat


def create_mission(db: Session, mission: MissionCreate) -> Mission:
    db_mission = Mission(is_complete=mission.is_complete)

    for target_data in mission.targets:
        target = Target(**target_data.model_dump())
        db_mission.targets.append(target)

    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


def get_mission(db: Session, mission_id: str) -> Mission:
    if not mission_id:
        raise HTTPException(status_code=400, detail="mission_id must be provided")

    try:
        mission_uuid = uuid.UUID(mission_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    db_mission = db.query(Mission).filter(Mission.id == mission_uuid).first()
    if not db_mission:
        raise HTTPException(status_code=404, detail="Cat not found Mission")
    return db_mission


def get_list_missions(db: Session, skip: int = 0, limit: int = 10) -> list[Mission]:
    return db.query(Mission).offset(skip).limit(limit).all()


def update_mission(db: Session, mission_id: str, mission_update: MissionUpdate):
    import uuid

    if not mission_id:
        raise HTTPException(status_code=400, detail="mission_id must be provided")

    try:
        mission_uuid = uuid.UUID(mission_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid mission UUID")

    mission = db.query(Mission).filter(Mission.id == mission_uuid).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")

    # Update mission is_complete if provided
    if mission_update.is_complete is not None:
        mission.is_complete = mission_update.is_complete

    # Prepare existing targets dict by id for quick lookup
    existing_targets = {str(t.id): t for t in mission.targets}

    # Collect IDs of incoming targets to check for removals
    incoming_target_ids = set()

    for t_in in mission_update.targets:
        if t_in.id:
            tid = str(t_in.id)
            incoming_target_ids.add(tid)

            if tid in existing_targets:
                target = existing_targets[tid]
                # You can add validation if mission or target is_complete blocks editing notes
                if mission.is_complete or target.is_complete:
                    raise HTTPException(
                        status_code=400,
                        detail="Cannot update target: mission or target is completed",
                    )
                # Update fields
                target.name = t_in.name
                target.country = t_in.country
                target.notes = t_in.notes
                target.is_complete = t_in.is_complete
            else:
                raise HTTPException(status_code=400, detail=f"Target with id {tid} not found")
        else:
            # New target, create and add
            new_target = Target(
                mission_id=mission.id,
                name=t_in.name,
                country=t_in.country,
                notes=t_in.notes,
                is_complete=t_in.is_complete or False,
            )
            db.add(new_target)

    # Optional: remove targets that are in DB but missing in update request
    for tid, target in existing_targets.items():
        if tid not in incoming_target_ids:
            db.delete(target)

    db.commit()
    db.refresh(mission)
    return mission


def delete_mission(db: Session, mission_id: str) -> Cat:
    if not mission_id:
        raise HTTPException(status_code=400, detail="mission_id must be provided")

    try:
        mission_uuid = uuid.UUID(mission_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    db_mission = db.query(Mission).filter(Mission.id == mission_uuid).first()
    if not db_mission:
        raise HTTPException(status_code=404, detail="Cat not found Mission")

    if db_mission.cat_id is not None:
        raise HTTPException(
            status_code=400, detail="Cannot delete: mission already assigned to a cat"
        )

    db.delete(db_mission)
    db.commit()
    return db_mission


def assign_cat_to_mission(db: Session, mission_id: str, cat_id: str) -> Mission:
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")

    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")

    mission.cat_id = cat.id
    db.commit()
    db.refresh(mission)
    return mission