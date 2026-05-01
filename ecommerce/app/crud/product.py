from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(Product).all()
#functions help us to connect to database that are called in request 
#crud delete 
#crud update

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()