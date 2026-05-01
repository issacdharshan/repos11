from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.crud.product import create_product,get_products,get_product
from app.schemas.product import ProductCreate,ProductResponse
router =APIRouter(prefix="/products",tags=['Products'])
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",response_model=ProductResponse)
def create(product:ProductCreate,db:Session=Depends(get_db)):
    return create_product(db,product)

@router.get("/get/products",response_model=list[ProductResponse])  
def read_all(db:Session=Depends(get_db)):
    return get_products(db)

@router.get("/{product_id}",response_model=ProductResponse)
def read_one(product_id:int,db:Session=Depends(get_db)):
    return get_product(db,product_id)    

    