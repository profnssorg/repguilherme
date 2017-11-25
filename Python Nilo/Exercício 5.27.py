#------------------------------------------------------------------------------
# Verifica se um número é palíndromo (continua igual com os dígitos invertidos)
#------------------------------------------------------------------------------

while True:

    n = int(input("Verificar se é palíndromo (0 para sair): "))

    if n == 0:
        break

    text = str(n)
    newt = ""
    x = 0

    while x < len(text):

        newt += text[-x-1]

        x += 1

    number = int(newt)

    if number == n:
        print("%d é palíndromo!" % n)
    else:
        print("%d não é palíndromo, pois %d é diferente de %d" % (n, n, number))
    

    print("\n")
