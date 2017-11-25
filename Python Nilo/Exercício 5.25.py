#----------------------------------------------------------
# Raiz quadrada de um número, utilizando o método de Newton
#----------------------------------------------------------

while True:
    n = float(input("Calcular raiz quadrada de (0 para sair): "))

    if n == 0:
        break
    elif n < 0:
        print ("Favor inserir um número positivo")
    else:

        b = 2.0
        p = 2.0

        while abs((p ** 2) - n) > 0.0001:
            p = (b + (n / b)) / 2
            b = p

        print ("%5.4f" % p)

    print("\n")
