#------------------------------------------------
# Organização de lugares vagos em salas de cinema
#------------------------------------------------

lugares_vagos = []
n = 0

while True:
    x = int(input("Lugares iniciais da sala %d (0 para terminar): " % (n + 1)))

    if x == 0:
        break
    
    lugares_vagos.append(x)
    n += 1

print("\n")

while True:
    sala = int(input("Selecionar sala (0 para terminar): "))

    if sala == 0:
        break
    elif sala < 1 or sala > len(lugares_vagos):
        print("Sala inválida")
    else:
        lugares = int(input("Quantos lugares você deseja? (%d vagos): " % lugares_vagos[sala-1]))

        if lugares > lugares_vagos[sala-1]:
            print("Número de lugares não disponível")
        elif lugares <= 0:
            print("Número inválido")
        else:
            lugares_vagos[sala-1] -= lugares
            print ("%d lugares vendidos!" % lugares)

    print("\n")

    print("Situação das salas: ")
    for n, x in enumerate(lugares_vagos):
        print("Sala %d - %d lugares vagos" % (n + 1, x))

    print ("\n")
    


    
