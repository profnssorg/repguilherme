# Nome do Pograma: Números Primos
# Autor: Guilherme Mendes
# Descrição: Exibe os N primeiros números primos


while True:
    
    n = int(input("Exibir os N primeiros primos (0 para sair): "))

    if n == 0:
        break

    primos = [2]
    x = 2

    while len(primos) < n:
        for p in primos:
            if x % p == 0:
                break
        else:
            primos.append(x)
                
        x += 1

    print (str(primos) + "\n")
        
