from sqlalchemy.orm import Session
from . import models, schemas

def get_record(db: Session, record_id: int):
    return db.query(models.Record).filter(models.Record.id == record_id).first()

def get_records(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Record).offset(skip).limit(limit).all()

def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.Record(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def update_record(db: Session, record_id: int, record: schemas.RecordUpdate):
    db_record = db.query(models.Record).filter(models.Record.id == record_id).first()
    if db_record:
        db_record.first_name = record.first_name or db_record.first_name
        db_record.last_name = record.last_name or db_record.last_name
        db_record.phone = record.phone or db_record.phone
        db_record.city = record.city or db_record.city
        db.commit()
        db.refresh(db_record)
        return db_record
    else: return None

def delete_record(db: Session, record_id: int):
    db_record = db.query(models.Record).filter(models.Record.id == record_id).first()
    if db_record:
        db.delete(db_record)
        db.commit()
        return {"message": "Record deleted successfully"}
    else:
        return None
