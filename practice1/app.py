import falcon
from customersresource import CustomerResource
app=falcon.App()

app.add_route("/customer",CustomerResource())