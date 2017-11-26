## Nome do Programa: Banco
## Autor: Guilherme Mendes
## Descrição: Estabele um sistema de Banco em Python
## Versão: 1.0
## Data: 26/11/2017


## Definição de classes

class Banco:
    '''
    Classe responsável pelo gerenciamento das funcionalidades do banco
    '''
    
    ## Definição de funções
    
    def __init__(self, nome):
        '''
        Inicializa o sistema
            nome : nome do banco
        '''
        
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abre_conta(self, conta):
        '''
        Abre uma nova conta
            conta : nome da conta
        '''
        self.contas.append(conta)

    def lista_contas(self):
        '''
        Mostra um resumo de todas as contas
        '''
        
        for c in self.contas:
            c.resumo()
           
        
class Cliente:
    '''
    Classe responsável por construir as informações dos clientes
    '''
    
    ## Definição de funções
    
    def __init__(self, nome, telefone):
        '''
        Inicializa o sistema
            nome : nome do cliente
            telefone : telefone do cliente
        '''
        
        self.nome = nome
        self.telefone = telefone
        
        
class Conta:
    '''
    Classe responsável por construir as informações das contas dos clientes
    '''
    
    def __init__(self, clientes, número, saldo=0):
        '''
        Inicializa o sistema
            clientes : clientes que são donos da conta
            número : número da conta
            saldo : saldo da conta
        '''
        
        self.clientes = clientes
        self.número = número
        self.saldo = 0

        self.operações = []
        self.depósito(saldo)

    def resumo(self):
        '''
        Mostra um resumo das informações da conta
        '''
        
        print ("CC Número: %s Saldo: %10.2f" % (self.número, self.saldo))
        
        for c in self.clientes:
            print ("  %s - %s" % (c.nome, c.telefone))

        print ("\n")

    def saque(self, valor):
        '''
        Implementa a opção de saque
            valor : valor a ser sacado
        '''
        
        if self.pode_sacar(valor) == True:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])

            return True
        else:
            print ("Saldo insuficiente")
            return False

    def pode_sacar(self, valor):
        '''
        Retorna se o cliente pode sacar o valor ou não
            valor : valor a ser sacado
        '''
        
        if self.saldo >= valor:
            return True
        else:
            return False

    def depósito(self, valor):
        '''
        Implementa a ação de depósito
            valor : valor a ser depositado
        '''
        
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        '''
        Mostra o extrato da conta
        '''
        
        print ("Extrato CC Número: %s\n" % self.número)

        for tipo, valor in self.operações:
            print ("%10s: %10.2f" % (tipo, valor))

        print ("\n     Saldo: %10.2f\n" % self.saldo)

        
        
class ContaEspecial(Conta):
    '''
    Classe responsável por implementar contas especiais, em que o cliente pode ficar deficitário
    '''
    
    def __init__(self, clientes, número, saldo=0, limite=0):
        '''
        Inicializa o sistema
            clientes : clientes que são donos da conta
            número : número da conta
            saldo : saldo da conta
            limite : limite de endividamento
        '''
        
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def extrato(self):
        '''
        Exibe o extrato da conta
        '''
        
        print ("Limite ---- %d" % self.limite)
        Conta.extrato(self)

    def pode_sacar(self, valor):
        '''
        Retorna se o cliente pode sacar o valor
            valor : valor a ser sacado
        '''
        
        if self.saldo + self.limite >= valor:
            return True
        else:
            return False
