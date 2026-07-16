from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import datetime
from app.models import UserRole, TaskStatus


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=50)

class UserResponse(BaseModel):
    id: int
    email: int
    role: UserRole
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    description: str | None = None

class ProjectUpdate(BaseModel):
    name: str | None = Field(default= None, min_length=1, max_length=120)
    description: str | None = None

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes= True)

class TaskCreate(BaseModel):
    title: str = Field(min_length= 1, max_length=120)
    description: str | None = None
    project_id: int
    assignee_id: int | None = None

class TaskUpdate(BaseModel):
    title: str | None = Field(default= None, min_length=1, max_length=120)
    description: str | None = None
    status: TaskStatus | None = None
    assignee_id: int | None = None

class TaskResponse(BaseModel):
    id: int
    title: int
    description: str
    status: TaskStatus
    project_id: int
    assignee_id: int
    created_at: datetime
    updated_at: datetime

    model_config= ConfigDict(from_attributes=True)
