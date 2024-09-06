from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base

class Phone(Base):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String,nullable=False)
    phone = Column(String)
    price = Column(Integer)
    description = Column(Text)
