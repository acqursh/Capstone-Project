from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from Models.users import User

Base = declarative_base()


class User_attr(Base):
    __tablename__ = 'user_attr'

    user_id = Column(String(45), ForeignKey(User.user_id), primary_key=True)
    age = Column(Integer)
    sex = Column(String(10))
    cp = Column(Integer)
    trestbps = Column(Integer)
    chol = Column(Integer)
    fbs = Column(Integer)
    restecg = Column(Integer)
    thalach = Column(Integer)
    exang = Column(Integer)
    oldpeak = Column(Float)
    slope = Column(Integer)
    ca = Column(Integer)
    thal = Column(Integer)
    target = Column(Integer)
