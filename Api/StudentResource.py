import json
from Create_table4 import Student
from Create_table4 import session


def on_put(req, resp):
    try:
        result = session.query(Student).filter(Student.id == 5).first()
        data = json.load(req.bounded_stream)
        result.name = data['name']
        result.marks = data['marks']
        result.age = data['age']
        session.commit()
    except Exception as e:
        raise Exception(e)
    else:
        resp.text = "result updated successfully."


class StudentResource:

    def on_post(self, req, resp):

        try:
            data = json.load(req.bounded_stream)
            result = Student(id=data['id'], name=data['name'], marks=data['marks'], age=data['age'])
            session.add(result)
            session.commit()
        except Exception as e:
            session.rollback()
            raise Exception(e)
        else:
            resp.text = "result added successfully."
        pass
    def on_get(self, req, resp):
        try:
            rows = session.query(Student).all()
            data = []
            for row in rows:
                data.append({"id": row.id, "name": row.name, "marks": row.marks, "age": row.age})
        except Exception as e:
            session.rollback()
            raise Exception(e)
        else:
            resp.text = json.dumps(data)
        pass

    def on_delete(self, req, resp):
        try:
            session.query(Student).filter(Student.id == 4).delete()
            session.commit()
        except Exception as e:
            raise Exception(e)
        else:
            resp.text = "deleted successfully."

        pass

    def on_patch(self, req, resp):
        try:
            result = session.query(Student).filter(Student.name == "manu").first()
            data = json.load(req.bounded_stream)
            result.marks = data['marks']
            result.age = data['age']
            session.commit()
        except Exception as e:
            raise Exception(e)
        else:
            resp.text = "result updated successfully."


