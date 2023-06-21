from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind = engine)

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key =  True)
   name = Column(String)
   address = Column(String)
   email = Column(String)


Base.metadata.create_all(engine)
session=Session()



def insert_data(session):

   data= Customers (name='Ramesh',address='VJWD',email='K@123')
   session.add(data)
   session.commit()

insert_data(session)


