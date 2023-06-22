from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_
from sqlalchemy import and_
#from sqlalchemy.orm.exc import MultipleResultsFound

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind = engine)

class Department(Base):
   __tablename__ = 'departments'
   id = Column(Integer, primary_key =  True)
   name = Column(String)
   address = Column(String)
   email = Column(String)

#Base.metadata.create_all(engine)
session=Session()

#def insert_data(session):

   #data = Department(name='Ramesh', address='VJWD', email='K@123')
   #session.add(data)
   #session.commit()


#insert_data(session)

# 1.Get all data
#result=session.query(Department)
#for values in result:
   #print(values.name,values.address,values.email)

#result = session.query(Department).filter(Department.id==2).all()
#for values in result:
   #print(values.name,values.address,values.email)

#2. Get data in Order
#data=session.query(Department).order_by(Department.name)
#for values in data:
   #print(values.name)
#query = session.query(Department).order_by(Department.id).all()
#for values in query:
   #print(values.id)

# Get data by filtering

#first()
#data=session.query(Department).first()
#print(data.name,data.address,data.email,data.id)

#data=session.query(Department).filter(Department.name=="Kavita").first()
#print(data.name,data.address,data.email)

#or()

#data=session.query(Department).filter(or_(Department.name=="Kavita",Department.name=="Rani"))
#for values in data:
   #print(values.name,values.address)

#and()

#data=session.query(Department).filter(and_(Department.name=="Kavita",Department.address=="KHM"))
#for values in data:
   #print(values.name,values.email)

#IN()

#data=session.query(Department).filter(Department.name.in_(["Rani","Kavita","Ramesh"]))
#for values in data:
   #print(values.id,values.name,values.address)

#notIN()
#data=session.query(Department).filter(~Department.name.in_(["Anita","Ramesh"]))
#for values in data:
   #print(values.name,values.address)

#one()
#data=session.query(Department).filter(Department.name=="Kavita").one()
#print(data.name,data.address,data.email)

#data=session.query(Department).one()
#try:
    #data = session.query(Department).one()
#except MultipleResultsFound:
   # Handle the case where multiple results are found
   #pass

#count the number of results
#data_count=session.query(Department).filter(or_(Department.name=="Kavita",Department.name=="Rani")).count()
#print(data_count)

#distinct()
#data=session.query(Department.name).distinct()
#for values in data:
   #print(values)

#Join()
#data=session.query(Department).join(Employee).all()
#for values in data:
   #print(Employee.name,Department.address)

#Rollback()

#data=session.query(Department).filter(Department.id==2).first()
#session.delete(Department del)
#session.commit()

session.delete('Rani')
session.query(Department).filter_by(name='Rani').count()















