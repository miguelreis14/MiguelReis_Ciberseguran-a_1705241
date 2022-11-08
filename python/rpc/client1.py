import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
x= int(input("entre o 1-valor: "))
y=int(input("entre o 2-valor: "))
print(type(x))
print(s.add(x,y))
print(s.sub(x,y))
print(s.multi(x,y))
print(s.div(x,y))

# Print list of available methods
print(s.system.listMethods())