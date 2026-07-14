from app.db.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, Boolean, Enum, DateTime, func, Text, ForeignKey
import enum
from datetime import datetime

class UserRole(str, enum.Enum):
    user = "user"
    admin = "admin"

class TaskStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    email: Mapped[str] = mapped_column(String(255), index= True, unique= True, nullable= False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable= False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default= UserRole.user, nullable= False)
    is_active: Mapped[bool] = mapped_column(Boolean, default= True, nullable= False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default= func.now(), nullable=False)

    projects: Mapped[list["Project"]] = relationship("Project", back_populates="owner", cascade="all, delete-orphan")
    tasks: Mapped[list["Task"]] = relationship("Task", back_populates= "assigned_to", cascade= "all, delete-orphan")

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable= False, index= True)
    description: Mapped[str] = mapped_column(Text, nullable= True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable= False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable= False)

    owner: Mapped["User"] = relationship("User", back_populates="projects")
    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="project", cascade= "all, delete-orphan")

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    title: Mapped[str] = mapped_column(String(255), index= True, unique= True, nullable= False)
    description: Mapped[str] = mapped_column(Text, nullable= True)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default= TaskStatus.todo, nullable=False, index= True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id", ondelete= "CASCADE"), nullable= False)
    assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete= "CASCADE"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default= func.now(), nullable=False)

    project: Mapped["Project"] = relationship("Project", back_populates="tasks")
    owner: Mapped["User"] = relationship("User", back_populates="tasks")

