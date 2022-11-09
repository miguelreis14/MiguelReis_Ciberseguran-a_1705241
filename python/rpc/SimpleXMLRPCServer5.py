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
    def supercomplex(a1,b1,a2,b2,test,teste2):
        o = complex(test)
        p = complex(teste2)

        return str (o+p)


    server.register_function(supercomplex, 'complex')

    # Run the server's main loop
    server.serve_forever()

