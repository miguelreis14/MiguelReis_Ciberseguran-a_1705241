import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
x= int(input("entre o 1-valor: "))
y=int(input("entre o 2-valor: "))

print(s.mul(x,y))  # Returns 5*2 = 10
print(s.sub(x,y))
print(s.poli(x))

# Print list of available methods
print(s.system.listMethods())