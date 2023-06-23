from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'student2'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    marks = Column(Integer)
    age = Column(Integer)


Base.metadata.create_all(engine)
session = Session()
