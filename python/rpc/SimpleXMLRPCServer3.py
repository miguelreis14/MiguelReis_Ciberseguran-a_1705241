from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()



    # Register a function under a different name
    def somatorion(x):
        i = 1
        total = 0
        while i <= x:
            total = total + (i ** 3)
            i=i+1
        return total

    server.register_function(somatorion, 'som')




    # Run the server's main loop
    server.serve_forever()

