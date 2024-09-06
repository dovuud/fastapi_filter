from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PhoneBase(BaseModel):
    brand_name: str
    phone: str
    price: int
    description: str

class PhoneCreate(PhoneBase):
    pass

class Phone(PhoneBase):
    id: int

    class Config:
        orm_mode = True