import xmlrpc.client
# ligacao ao server
s = xmlrpc.client.ServerProxy('http://localhost:8000')

x=0
y=0
# Verificacao de valores incorretos e call para o server
while x == 0 or y == 0:
    x = int(input("Introduza o primeiro numero "))
    y = int(input("Introduza o segundo numero "))
    if (x == 0 or y == 0):
        print("Erro nos valores, tente outra vez")
    else:
        print(s.isdiv(x, y))
        break;


