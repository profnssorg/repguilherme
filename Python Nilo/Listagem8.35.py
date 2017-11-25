#-----------------------------------------------------------
# Exemplo de função (soma) que imprime um módulo (validação)
#-----------------------------------------------------------

import Listagem8_34


def soma():
    L = []

    for x in range(10):
        L.append(Listagem8_34.valida_inteiro("Digite um número: ", 0, 20))

    print("Soma: %d" % sum(L))

soma()
