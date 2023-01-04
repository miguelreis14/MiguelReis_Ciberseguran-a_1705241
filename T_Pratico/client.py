import xmlrpc.client

# ligacao ao server
s = xmlrpc.client.ServerProxy('http://localhost:8000')
# iniciar varieaveis a strings
x = '0'
y = '0'
# Verificacao de valores incorretos e call para o server
# funcao isnumeric
while x == '0' or y == '0' or x.isnumeric() == False or y.isnumeric() == False:
    x = (input("Introduza o primeiro numero "))
    y = (input("Introduza o segundo numero "))

    if x == '0' or '0' == 0 or x.isnumeric() == False or y.isnumeric() == False:
        print("Erro nos valores, tente outra vez")
    else:
        # importante fazer cast para int
        print(s.isdiv(int(x), int(y)))
        break
