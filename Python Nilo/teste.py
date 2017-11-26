## Nome do Programa: Teste do programa Banco
## Autor: Guilherme Mendes
## Descrição: Testa o sistema de Banco anteriormente criado
## Versão: 1.0
## Data: 26/11/2017

## Importação de módulos
from banco import Banco
from contas import Conta, ContaEspecial
from clientes import Cliente

## Definição de variáveis
joão = Cliente("João", "123-456")
josé = Cliente("José", "567-890")
maria = Cliente("Maria", "321-532")

# Cria as contas
contaJM = Conta([joão, maria], 1, 1000)
contaJ = ContaEspecial([josé], 2, 1000, 100)

# Cria o banco
tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)

tatu.lista_contas()

# Estabelece operações
contaJM.saque(1050)
contaJ.saque(1050)
contaJ.extrato()
