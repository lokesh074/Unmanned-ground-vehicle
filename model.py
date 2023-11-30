from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
import database
from datetime import datetime
from database import Base
class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    is_human = Column(Boolean, default=False)
    found = Column(DateTime, default=func.now())
