from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.database import Base, engine, SessionLocal
from app.users.routers import router as auth_router
from app.routers.products import router as products_router 



# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency for getting the DB session


# FastAPI app initialization
app = FastAPI()

app.include_router(products_router)
app.include_router(auth_router)


