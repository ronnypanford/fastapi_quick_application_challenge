from typing import Optional

from sqlalchemy import Column, Integer, String, Float, DateTime, func

from database_config.database import Base


class User(Base):

    __tablename__ = "Users"

    ID = Column(Integer, primary_key=True, index=True, nullable=False)
    NAME = Column(String(30), index=True, nullable=False)
    WEIGHT = Column(Float(2), nullable=False)
    DESCRIPTION = Column(String, nullable=True, default="")

    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())
