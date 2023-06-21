from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
meta = MetaData()
conn=engine.connect()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String)
)
meta.create_all(engine)

conn.execute(students.insert(), [
    {'name':'Ravi','lastname':'Kapoor'},
    {'name':'Rajiv','lastname':'Khanna'},
    {'name':'Komal','lastname':'Bhandari'},
    {'name':'Abdul','lastname':'Sattar'}
])
s=students.select()

conn=engine.connect()
result=conn.execute(s)

for row in result:
    print(row)


