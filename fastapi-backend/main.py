import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, config
from .database import SessionLocal, engine
from .cache import init_cache, cache, redis_cache
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from .config import settings


FRONTEND_URL = settings.FRONTEND_URL

models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_cache()
    yield
    await redis_cache.close()

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.on_event("startup")
async def startup_event():
    init_cache()


@app.get("/")
def root():
    return "Welcome to records api!"

@app.get("/records", response_model=list[schemas.Record])
@cache(expire=60)
async def get_records(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    await asyncio.sleep(2)
    records = crud.get_records(db, skip=skip, limit=limit)
    return records

@app.post("/records", response_model=schemas.Record)
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    return crud.create_record(db=db, record=record)

@app.get("/records/{record_id}", response_model=schemas.Record)
@cache(expire=60)
async def get_record(record_id: int, db: Session = Depends(get_db)):
    await asyncio.sleep(2)
    record = crud.get_record(db=db, record_id=record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found!")
    return record


@app.put("/records/{record_id}", response_model=schemas.Record)
async def update_record(record_id: int, record: schemas.RecordUpdate, db: Session = Depends(get_db)):
    record = crud.update_record(db=db, record_id=record_id, record=record)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found!")
    return record

@app.delete("/records/{record_id}", response_model=schemas.Record)
def delete_record(record_id: int, db: Session = Depends(get_db)):
    record = crud.delete_record(db=db, record_id=record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found!")
    else: return record

