      #CRUD LIKE FILE FOR USER AUTH LIKE DATABASE
from sqlalchemy.orm import Session
from app.users import models, schemas 
from app.core.security import hash_password, verify_password,create_access_token


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(email=user.email,hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
def login_user(db:Session,user_data):
    user=authenticate_user(db,user_data.email,user_data.password)
    if not user:
        return None
    
    token =create_access_token({"sub":user.email})
    return token