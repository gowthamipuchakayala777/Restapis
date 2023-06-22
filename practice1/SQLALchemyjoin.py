from create_table2 import Customers
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind = engine)

class Employee(Base):
   __tablename__ = 'employee1'
   id = Column(Integer, primary_key =  True)
   firstname = Column(String)
   lastname = Column(String)
   gender = Column(String)
   country = Column(String)
   age = Column(Integer)

Base.metadata.create_all(engine)
session=Session()

#def insert_data(session):

   #data = Employee(id=5,firstname="Ira",lastname="Beak",gender="Female",country="UK",age=13)
   #session.add(data)
   #session.commit()

#insert_data(session)

#result=session.query(Employee,Customers).join(Customers).all()
#for employee,customers in result:
   #print(employee.firstname,customers.gender)

data=Employee(id=6,firstname="Mara",lastname="drag",gender="Female",country="USA",age=24)
session.add(data)

session.query(Employee).filter(Employee.firstname.in_(['Bhavani', 'Mara'])).all()
session.rollback()



