class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.clientes = clientes
        self.número = número
        self.saldo = 0

        self.operações = []
        self.depósito(saldo)

    def resumo(self):
        print ("CC Número: %s Saldo: %10.2f" % (self.número, self.saldo))
        
        for c in self.clientes:
            print ("  %s - %s" % (c.nome, c.telefone))

        print ("\n")

    def saque(self, valor):
        if self.pode_sacar(valor) == True:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])

            return True
        else:
            print ("Saldo insuficiente")
            return False

    def pode_sacar(self, valor):
        if self.saldo >= valor:
            return True
        else:
            return False

    def depósito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print ("Extrato CC Número: %s\n" % self.número)

        for tipo, valor in self.operações:
            print ("%10s: %10.2f" % (tipo, valor))

        print ("\n     Saldo: %10.2f\n" % self.saldo)

class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def extrato(self):
        print ("Limite ---- %d" % self.limite)
        Conta.extrato(self)

    def pode_sacar(self, valor):
        if self.saldo + self.limite >= valor:
            return True
        else:
            return False






        
