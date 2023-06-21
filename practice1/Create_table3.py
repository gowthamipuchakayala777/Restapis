from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind = engine)
from googlesheet import source


class Customers(Base):
   __tablename__ = 'customers1'
   id = Column(Integer, primary_key =  True)
   firstname = Column(String)
   lastname = Column(String)
   gender = Column(String)
   country = Column(String)
   age = Column(Integer)


   def todict(self):
      result= {"id":self.id,
               "firstname":self.firstname,
               "lastname":self.lastname,
               "gender":self.gender,
               "country":self.country,
               "age":self.age}
      return result


Base.metadata.create_all(engine)
session=Session()


data = source()
for result in data:
   row= Customers(firstname=result['First Name'] ,lastname=result['Last Name'],gender=result['Gender'],country=result['Country'],age=result['Age'])
   session.add(row)
session.commit()

