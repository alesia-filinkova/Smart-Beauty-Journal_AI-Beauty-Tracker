from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True

class HealthLogBase(BaseModel):
    sleep_hours: float
    water_intake: float
    stress_level: int
    menstruation: bool
    meals: int
    weather: str
    mood: str
    weight: float

class HealthLogCreate(HealthLogBase):
    date: date

class HealthLog(HealthLogBase):
    id: int
    user_id: int
    date: date
    class Config:
        orm_mode = True
