from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Donor(Base):
    __tablename__ = 'donors'
    donor_id = Column(Integer, primary_key=True)
    hla_typing = Column(String)
    blood_group = Column(String)
    weight = Column(Float)
    height = Column(Float)
    nature_of_ailment = Column(String)
    address = Column(String)
