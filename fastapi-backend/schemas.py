from pydantic import BaseModel
from typing import Optional

class RecordBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    city:str
    
class RecordCreate(RecordBase):
    pass

class RecordUpdate(RecordBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None

class Record(RecordBase):
    id: int

    class ConfigDict:
        from_attributes = True

