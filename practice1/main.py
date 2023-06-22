import falcon
from customersresource import CustomerResource
from wsgiref.simple_server import make_server
from waitress import serve

app=falcon.App()

app.add_route("/customer",CustomerResource())
if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd .serve_forever()