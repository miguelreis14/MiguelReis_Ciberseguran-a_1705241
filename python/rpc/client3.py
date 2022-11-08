import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
x= int(input("entre o 1-valor: "))



print(s.som(x))

# Print list of available methods
print(s.system.listMethods())