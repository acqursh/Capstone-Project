from sqlalchemy import Column, Float, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(String(45), primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    access_token = Column(String(950))
    gender = Column(String(10))
    weight = Column(Float)
    age = Column(Integer)
    create_time = Column(DateTime(timezone=True), default=func.now())
