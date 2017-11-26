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
