from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import User
from app.core.security import hash_password, verify_password
from app.schemas import UserCreate

def create_user(user: UserCreate, db: Session):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail= "Email already registered")

    new_user = User(email = user.email, hashed_password = hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if user is None or not verify_password(password, user.hashed_password):
        return None
    return user
