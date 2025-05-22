from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel, Field


class TargetBase(BaseModel):
    name: str
    country: str
    notes: Optional[str] = None
    is_complete: Optional[bool] = False


class TargetCreate(TargetBase):
    pass


class TargetUpdate(BaseModel):
    notes: Optional[str] = None
    is_complete: Optional[bool] = None


class TargetOut(TargetBase):
    id: UUID
    mission_id: UUID

    class Config:
        from_attributes = True


class CatBase(BaseModel):
    name: str
    breed: str
    salary: int


class CatCreate(CatBase):
    pass


class CatUpdate(BaseModel):
    salary: int


class CatOut(CatBase):
    id: UUID

    class Config:
        from_attributes = True


class MissionBase(BaseModel):
    is_complete: Optional[bool] = False


class MissionCreate(MissionBase):
    targets: List[TargetCreate]


class MissionAssignCat(BaseModel):
    cat_id: UUID


class MissionOut(MissionBase):
    id: UUID
    cat_id: Optional[UUID]
    targets: List[TargetOut]

    class Config:
        from_attributes = True


class TargetUpdate(BaseModel):
    id: Optional[UUID]
    name: str
    country: str
    notes: Optional[str] = None
    is_complete: Optional[bool] = False

class MissionUpdate(BaseModel):
    is_complete: Optional[bool] = False
    targets: List[TargetUpdate]