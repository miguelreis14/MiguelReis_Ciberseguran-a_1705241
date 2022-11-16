from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Crear servidor port 8000
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # funcao se é divisivel
    def isdiv(x, y):
        if x % y == 0:
            ss = str(x) + " é divisivel por " + str(y)
            return ss

        else:
            ss = str(x) + " nao é divisivel por " + str(y)
            return ss

    # registar funcao
    server.register_function(isdiv, 'isdiv')
    # server loop
    server.serve_forever()
