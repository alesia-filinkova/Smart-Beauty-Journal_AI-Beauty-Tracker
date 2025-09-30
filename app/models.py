from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    health_logs = relationship("HealthLog", back_populates="user")

class HealthLog(Base):
    __tablename__ = "health_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    sleep_hours = Column(Float)
    water_intake = Column(Float)
    stress_level = Column(Integer)
    menstruation = Column(Boolean)
    meals = Column(Integer)
    weather = Column(String)
    mood = Column(String)
    weight = Column(Float)
    
    user = relationship("User", back_populates="health_logs")
