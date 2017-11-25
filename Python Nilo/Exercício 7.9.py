#----------------------------
# Jogo da forca
#----------------------------

import random

lista = ["abacate", "teste", "xerox", "casa", "caneta", "livro", "forca", "passarinho", "cama", "bola", "avestruz", "estojo",
         "novato", "python", "programa", "livro", "livraria", "futebol", "mochila", "celular", "teclado", "tecla", "apontardor",
         "grampo", "azul", "papel", "camiseta", "casaco", "quadro", "texto"]

indice = random.randint(0, len(lista)-1)

palavra = lista[indice].lower().strip()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""

    for letra in palavra:
        senha += letra if letra in acertos else "."


    print(senha)

    if senha == palavra:
        print ("Você acertou!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()

    if len(tentativa) > 1:
        print ("Digite apenas uma letra")
        continue

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue

    else:
        digitadas += tentativa

        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print ("Você errou!")

    print("X==:==\nX  :  ")
    print("X  0  " if erros >= 1 else "X")

    linha2 = list("X      ")
    
    if erros == 2:
        linha2[3] = "|"
    elif erros == 3:
        linha2[2:4] = "\|"
    elif erros >= 4:
        linha2[2:5] = "\|/"
    print("%s" % "".join(linha2))

    linha3 = list("X      ")

    if erros == 5:
        linha3[2] = "/"
    elif erros >= 6:
        linha3[2:5] = "/ \\"
    print("%s" % "".join(linha3))

    print("X\n=========")

    if erros == 6:
        print("Enforcado!\nA palavra era: %s" % palavra)
        break
