## Nome do Programa: Agenda
## Autor: Guilherme Mendes
## Descrição: Implementa um sistema simples de agenda em Python
## Versão: 1.0
## Data: 26/11/2017


## Definição de variáveis
agenda = []


## Definição de funções

def pede_nome():
    '''
    Pede para o usuário inserir um nome    
    '''
    
    return(input("Nome: "))

def pede_telefone(t="\n-- Adicionar Telefone --"):
    '''
    Pede para o usuário inserir um telefone
        t : texto de apoio
    '''
    
    print(t)
    tipo = input(" Tipo: ")
    
    num = input(" Número: ")

    return [tipo, num]

# 
def mostra_dados(nome, telefones, numero=-1):
    '''
    Mostra os dados dos contatos
        nome : nome a ser mostrado
        telefones : telefones a serem mostrados
        numero : o número do contato (-1 não mostra nada)
    '''
    
    n = ("%s" % nome).ljust(20)
    s = "" if numero == -1 else "{0}. ".format(numero)
    
    print("\n%sNome: %s" % (s, n))
    
    for t in telefones:
        print(" Telefone %s: %s" % (t[0], t[1]))

def pede_nome_arquivo():
    '''
    Pede o nome do arquivo
    '''
    
    return(input("Nome do arquivo: "))

def pesquisa(nome):
    '''
    Pesquisa um nome na agenda, e retorna sua posição
        nome : nome a ser pesquisado
    '''
    
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    '''
    Cria um novo contato
    '''
    
    global agenda

    nome = pede_nome()

    for nom, num in agenda:
        if nom == nome:
            print ("Esse nome já existe. (2) Para alterar")
            return

    t = [pede_telefone()]

    while mais_telefone() == True:
        t.append(pede_telefone(""))
        
    
    valida_novo_contato(nome, t)

def mais_telefone(t="Adicionar"):
    '''
    Dá a possibilidade de o usuário adicionar mais telefones
        t : texto de apoio
    '''
    
    while True:
        q = input("\n%s mais telefones? (S) ou (N): " % t)
        if q == "S":
            return True
        elif q == "N":
            return False
        else:
            print("Favor inserir uma resposta válida\n")
            

def apaga():
    '''
    Apaga um contato
    '''
    
    global agenda

    nome = pede_nome()
    p = pesquisa(nome)

    if p != None:
        if confirmar():
            del agenda[p]

    else:
        print("Nome não encontrado")

def altera():
    '''
    Altera um contato
    '''
    
    p = pesquisa(pede_nome())

    if p != None:

        if confirmar():

            nome = agenda[p][0]
            telefones = agenda[p][1]
            print("\n-- Encontrado --")
            mostra_dados(nome, telefones)

            print("\n-- Alterar Dados --")
            nnome = pede_nome()

            ntel = telefones[:]

            a = altera_telefone(telefones)

            if a[1] == -1:
                ntel.append([a[0][0], a[0][1]])
            else:
                ntel[a[1]] = a[0]

            while mais_telefone("Alterar") == True:
                a = altera_telefone(telefones)

                if a[1] == -1:
                    ntel.append([a[0][0], a[0][1]])
                else:
                    ntel[a[1]] = a[0]

            v = valida_novo_contato(nnome, ntel, 2)
            if v != None:
                agenda[p] = v               

    else:
        print ("Nome não encontrado")

def altera_telefone(telefones):
    '''
    Altera os telefones de um contato
    '''
    
    ntelefone = pede_telefone("")

    x = 0
    mudou = False
    index = -1

    for t in telefones:
        if t[0] == ntelefone[0]:
            index = x
            mudou = True

        x += 1
        
    return [ntelefone, index]
    

def lista():
    '''
    Exibe os dados da agenda
    '''
    
    print("\n-- Agenda --\n\n------")
    x = 1
    for e in agenda:
        mostra_dados(e[0], e[1], x)
        x += 1
    print("\n------\n")

def lê(forçar_nome=""):
    '''
    Carrega uma agenda salva
        forçar_nome : arquivo a ser aberto (vazio para pedir o nome ao usuário)
    '''
    
    global agenda

    if forçar_nome == "":
        nome_arquivo = pede_nome_arquivo()
    else:
        nome_arquivo = forçar_nome
    
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone = l.strip().split("#")

        tels = telefone.strip().split("$")
        del(tels[0])
 
        telefones = []
        for t in tels:
            telefones.append(t.split(","))
        
        agenda.append([nome, telefones])
    arquivo.close()

    salvar_referencia_arquivo(nome_arquivo)

def grava():
    '''
    Salva a agenda
    '''
    
    nome_arquivo = pede_nome_arquivo()

    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:

        num = ""
        for n in e[1]:
            num += "${0},{1}".format(n[0], n[1])
        
        arquivo.write("%s#%s\n" % (e[0], num))
    arquivo.close()

    salvar_referencia_arquivo(nome_arquivo)

def tamanho():
    '''
    Retorna o tamanho da agenda
    '''
    
    return len(agenda)

def confirmar():
    '''
    Janela para confirmação de operações
    '''
    
    result = None

    while result == None:
        ans = input("Confirmar operação? (S ou N) ")
        if ans == "S":
            result = True
        elif ans == "N":
            result = False
        else:
            print("Favor inserir resposta válida\n")

    return result


def valida_novo_contato(nome, telefones, tipo=1):    
    '''
    Retorna se o novo contato é válido ou não
        nome : novo nome
        telefones : novos telefones
        tipo : 1 adiciona o contato à agenda, se for válido; 2 apenas retorna o contato
    '''
    
    error = False

    for e in telefones:
        if e[0].find("#") != -1 or e[1].find("#") != -1:
            error = True
    
    if nome.find("#") != -1 or error:
        print("Contato inválido")
        return None
    else:
        if tipo == 1:
            agenda.append([nome, telefones])
        elif tipo == 2:
            return [nome, telefones]
        else:
            raise TypeError("Tipo inválido")

def valida_faixa_inteiro(pergunta, inicio, fim):
    '''
    Valida o retorno a uma pergunta feita ao usuário
        pergunta : texto a ser exibido para a pergunta
        inicio : menor valor aceitável
        fim : maior valor aceitável
    '''
    
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def salvar_referencia_arquivo(nome):
    '''
    Salva a referência do arquivo em que a agenda será salva/carregada
        nome : nome do arquivo
    '''
    
    global referencia

    referencia = nome

    salvar_ref = open("referencias.txt", "w")
    salvar_ref.write(referencia)
    salvar_ref.close

def carregar_referencia():
    '''
    Carrega a agena a partir do arquivo de referência salvo
    '''
    
    ref = open("referencias.txt", "r")
    lê(ref.readlines(0)[0])
    ref.close
    

def menu():
    '''
    Estabelece o menu da agenda
    '''
    
    print("\nAGENDA - %d pessoa(s)" % tamanho())
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê

0 - Sai
""")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


## Programa

try:
    carregar_referencia()
except:
    print("Bem-vindo a sua primeira utilização da agenda!")

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
    
