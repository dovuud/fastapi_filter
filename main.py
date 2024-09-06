from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/phone/", response_model=schemas.Phone)
async def create_phone(phone: schemas.PhoneCreate, db: Session = Depends(get_db)):
    db_phone = models.Phone(**phone.dict())
    db.add(db_phone)
    db.commit()
    db.refresh(db_phone)
    return db_phone

@app.get("/phone/", response_model=List[schemas.Phone])
async def get_phones(db: Session = Depends(get_db)):
    query = db.query(models.Phone)