from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional
from enum import Enum

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    
class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    
    class config:
        orm_mode = True
        
        
class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in progress"
    completed = "completed"        
        
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    status: TaskStatus      
    user_id: int
    
class TaskUpdate(BaseModel):
    status: TaskStatus
    
class Task(TaskCreate):
    id: int
    
    class config:
        orm_mode = True

                           