<p align="center">
Relatório do Trabalho prático<br />
Sistemas Distribuídos<br />
<br />
<br />
Verificar se um número é divisível
<br /> 
<br />
Aluno: Miguel Reis, 1705241,
<br />
miguelreis14, reisdmiguel@gmail.com
</p>
<br />

[**1. Descrição do Trabalho**](#descrição-do-trabalho) 

[**2. Função implementada**](#função-implementada) 

[**3. Servidor**](#servidor) 

[**4. Client**](#client) 

[**5. Funcionamento do trabalho**](#funcionamento-do-trabalho) 

[**6. Conclusão**](#conclusão) 

[**7. Bibliografia**](#bibliografia) 

## 

## Descrição do Trabalho

Neste trabalho estou a implementar uma função para determinar se um número é ou não divisível por outro numa arquitetura RPC.

## Função implementada

A minha função recebe dois números do cliente e utiliza o operador % para verificar se o resto da divisão é igual a 0.

## Servidor

```
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
```

Este código cria um servidor RPC na qual registo a função “isdiv” que recebe dois valores e executa um if para verificar se o primeiro número é divisível pelo segundo e de seguida envia o resultado para o cliente na forma de uma string.

## Client

```
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
```

Este código pede dois números ao utilizador e verifica se algum deles é 0 antes de os enviar ao servidor.

## Funcionamento do trabalho

![](./imagens/server.png)

Output do server

![](./imagens/1.png)

Verificação de erro no cliente

![](./imagens/3.png)

Output se é divisível

![](./imagens/4.png)

Output se não é divisível

## Conclusão

// descrever brevemente o que se fez e o que faltou fazer

## 

## Bibliografia
