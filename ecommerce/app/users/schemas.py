from pydantic import BaseModel, EmailStr,Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str= Field(min_length=6,max_length=72)

class UserLogin(BaseModel):
    email: EmailStr
    password: str
class Token(BaseModel):
    access_token:str
    token_type:str
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True