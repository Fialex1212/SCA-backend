import uuid
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.session import Base

class Cat(Base):
    __tablename__ = "cats"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True, nullable=False)
    breed = Column(String, nullable=True)
    salary = Column(Integer, nullable=True)

class Mission(Base):
    __tablename__ = "missions"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    cat_id = Column(UUID(as_uuid=True), ForeignKey("cats.id"), nullable=True)
    is_complete = Column(Boolean, default=False)

    cat = relationship("Cat", backref="missions")
    targets = relationship("Target", cascade="all, delete", backref="mission")


class Target(Base):
    __tablename__ = "targets"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    is_complete = Column(Boolean, default=False)

    mission_id = Column(UUID(as_uuid=True), ForeignKey("missions.id"))
