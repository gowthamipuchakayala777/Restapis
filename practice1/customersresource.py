from Create_table3 import Customers
from Create_table3 import session
import json

class CustomerResource():

    def on_get(self, req, resp):
        try:
            data=session.query(Customers).all()
            result=[]
            for row in data:
                print(row.todict())
                result.append(row.todict())
        except Exception as e:
            raise Exception(e)
        else:
            resp.text=json.dumps(result)
        pass

    def on_post(self,req,resp):
        try:
            data = json.load(req.bounded_stream)
            result = Customers( firstname=data['firstname'], lastname=data['lastname'],gender=data['gender'],country=data['country'],age=data['age'])
            session.add(result)
            session.commit()
        except Exception as e:
            session.rollback()
            raise Exception(e)
        else:
            resp.text = "result added successfully."
        pass

    def on_put(self, req, resp):
        try:
            result = session.query(Customers).filter(Customers.firstname =="Gaston" ).first()
            data = json.load(req.bounded_stream)
            result.lastname=data['lastname']
            result.gender=data['gender']
            result.country=data['country']
            result.age=data['age']
            session.commit()
        except Exception as e:
            raise Exception(e)
        else:
            resp.text = "result updated successfully."
        pass


    def on_delete(self, req, resp):
        try:
            session.query(Customers).filter(Customers.id == 4).delete()
            session.commit()
        except Exception as e:
            raise Exception(e)
        else:
            resp.text = "deleted successfully."
        pass

    def on_patch(self, req, resp):
        try:
            result = session.query(Customers).filter(Customers.firstname == "Philip").first()
            data = json.load(req.bounded_stream)
            result.lastname = data['lastname']
            result.gender = data['gender']
            session.commit()
        except Exception as e:
            raise Exception(e)
        else:
            resp.text = "result updated successfully."
        pass
