from pydantic import BaseModel
from typing import List, Optional

# User schema
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

# Product schema
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True

# Order schema
class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True
