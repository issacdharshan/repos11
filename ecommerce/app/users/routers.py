from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.routers.products import get_db
from app.users import schemas,services
from app.core.security import create_access_token,get_current_user



router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)


@router.post("/login",response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
   # db_user = services.authenticate_user(db, user.email, user.password)
    token =services.login_user(db,user)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(current_user:str=Depends(get_current_user)):
    return {"user":current_user}
