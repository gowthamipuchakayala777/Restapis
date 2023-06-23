import falcon
from StudentResource import StudentResource
from wsgiref.simple_server import make_server

app = falcon.App()

app.add_route("/student", StudentResource())
if __name__ == '__main__':
    try:
        with make_server('', 8000, app) as httpd:
            print('Serving on port 8000...')
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("Server stopped by the user. Exiting gracefully...")
