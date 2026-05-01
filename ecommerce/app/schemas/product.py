from pydantic import BaseModel,Field
class ProductBase(BaseModel):
    name:str =Field(...,min_length=3)
    description:str
    price:float=Field(...,gt=0)

class ProductCreate(ProductBase):
    pass 
class ProductResponse(ProductBase):
    id:int

    class Config:
        from_attributes=True
#delete schema and crud function

