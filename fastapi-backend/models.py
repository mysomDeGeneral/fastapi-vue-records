from sqlalchemy import String, Integer, Column
from .database import Base


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    city = Column(String)


