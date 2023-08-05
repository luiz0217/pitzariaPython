#
# variaveis
#
import os
from pessoa import pessoa
from clientes import clientes
from funcionario import funcionario
from queue import Queue
progAberto = True
logado = False

clientela = []

MdE = [Queue(maxsize=20),Queue(maxsize=20)] #modo de entrega entrega/balcão


tamanhos = ["pequena","media","grande"] 
sabores = ["calabreza","4 QUEIJO","farango com catupiri"]# <- pilha
extras = ["","lombo","bacon"]# <- pilha

logins = {"luiz":1234,"bruno":1234,"leo":1234}

#
#   função
#
def save(c = []):
    arqueCl = open("clientes.txt","w")
    for i in range(len(c)):
        if c[i] != "":
            arqueCl.write(c[i])
            #arqueCl.write("\n#)
    arqueCl.close()


def load():
    arqueCl = open("clientes.txt","r")
    for i in range(20):
        clientela.append(str(arqueCl.readline()))         
    arqueCl.close()

def cadastro(a = {}):
    leo = funcionario('Leonardo', 1234)
    leo.cadastro()
    a[leo._nome] = leo._numero    
    return a

def log(a = {}):
    c = input("LOGIN: ")
    v = int(input("SENHA: "))
    for chave,valor in a.items():
        if c == chave and valor == v:
            return True
    return False

def CadasClientes(a = []):
    select = int(input("|adicionar: 1|\n|deletar:   2|\n"))
    if select == 1:
        cliente = clientes("nome", 123, "endereco", "formaPagamento")
        cliente.cadastro()
        a.append(cliente._nome)
        a.append("\n")
    if select == 2:
        nome = input("nome do cliente: ")
        for n in a:
            if n == nome:
                a.remove(n)
    print(a)
    return a

def addSabores(pilha = []):
    pilha.append(input("digite o sabor a ser adicionado: "))
    print(pilha)
    return pilha

def remSabores(pilha = []):
    if len(pilha) == 0:
        print("vazia")
    else:
        pilha.pop()
        return pilha
    
def addExtras(pilha = []):
    pilha.append(input("digite o sabor a ser adicionado: "))
    print(pilha)
    return pilha

def remExtras(pilha = []):
    if len(pilha) == 0:
        print("vazia")
    else:
        pilha.pop()
        return pilha

def sabor(pilha = []):
    select = int(input("|adicionar: 1|\n|remover:   2|\n"))
    if select == 1:
        pilha = addSabores(pilha)
    if select == 2:
        pilha = remSabores(pilha)
    print(pilha)
    return pilha

def extra(pilha = []):
    select = int(input("|adicionar: 1|\n|remover:   2|\n"))
    if select == 1:
        pilha = addExtras(pilha)
    if select == 2:
        pilha = remExtras(pilha)
    print(pilha)
    return pilha

def pedidos(e = Queue(maxsize=20),b = Queue(maxsize=20)):
    select = int(input("|balcão:  1|\n|entrega: 2|\n"))
    print("selecione o cliente",clientela)
    cl = clientela[int(input()) - 1]
    print("selecione o tamanho",tamanhos)
    tamanho = tamanhos[int(input()) - 1]
    print("selecione o sabor",sabores)
    sabor = sabores[int(input()) - 1]
    print("selecione o extra",extras)
    extra = extras[int(input()) - 1]
    if select == 1:
        b.put([str(cl),str(tamanho),str(sabor),str(extra)])        
    if select == 2:
        e.put([cl,tamanho,sabor,extra])
    print("o preço da pizza é R$",preco(3,[cl,tamanho,sabor,extra]),",00")
    return e,b

def cozinha(e = Queue(maxsize=20),b = Queue(maxsize=20)):
    print("balcão",b.queue)
    print("entrega",e.queue)
    select = int(input("balcão: 1, entrega: 2 "))
    if select == 1:
        b.get()
    if select == 2:
        e.get()
    print("balcão",b.queue)
    print("entrega",e.queue)
    return e,b


def preco(a,p = []):
    if a < 0:
        return 0
    elif a == (3):
        for i in range(len(extras)):
            if (p[a]) == (extras[i]):
                return 2 * i  + preco(a-1,p)
    elif a == (2):
        for i in range(len(sabores)):
            if (p[a]) == (sabores[i]):
                return 3 * (i+1) + preco(a-1,p)
    elif a == (1):
        for i in range(len(tamanhos)):
            if (p[a]) == (tamanhos[i]):
                return 5 * (i+1)


#    CODIGO EM SI
#
# || || || || || || ||
# \/ \/ \/ \/ \/ \/ \/

load()
os.system('cls')
while progAberto == True:
   if logado == False: 
    select = int(input("|Login:    1|\n|Cadastro: 2|\n|Fechar:   3|\n"))
    if select == 1:
        logado = log(logins)
    if select == 2:
        logins = cadastro(logins)
    if select == 3:
        progAberto = False
   if logado == True:
    select = int(input("|Fazer um pedido: 1|\n|Cadastros:       2|\n|Cozinha:         3|\n|Sabores:         4|\n|Extras:          5|\n|Fechar:          6|\n"))
    if select == 1 and len(clientela) != 0:
        MdE = pedidos(MdE[0],MdE[1])
        print(MdE[0].queue,MdE[1].queue)
    if select == 2:
        CadasClientes(clientela)
    if select == 3:
        MdE = cozinha(MdE[0],MdE[1])
    if select == 4:
        sabor(sabores)
    if select == 5:
        extra(extras)
    if select == 6:
        progAberto = False
   save(clientela)

    
   

