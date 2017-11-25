from banco import Banco
from contas import Conta, ContaEspecial
from clientes import Cliente

joão = Cliente("João", "123-456")
josé = Cliente("José", "567-890")
maria = Cliente("Maria", "321-532")

contaJM = Conta([joão, maria], 1, 1000)

contaJ = ContaEspecial([josé], 2, 1000, 100)

tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)

tatu.lista_contas()


contaJM.saque(1050)
contaJ.saque(1050)
contaJ.extrato()
