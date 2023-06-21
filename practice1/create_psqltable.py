from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind = engine)
from googlesheet2 import source2


class Employee(Base):
   __tablename__ = 'employee'
   name = Column(String)
   id = Column(String)
   marks= Column(Integer,primary_key = True)
   section = Column(String)

Base.metadata.create_all(engine)

session=Session()


data = source2()
for result in data:
   # print(result)
    row = Employee(name=result['Name'],id=result['Id'],marks=result['Marks'],section=result['Section'])
    session.add(row)
session.commit()