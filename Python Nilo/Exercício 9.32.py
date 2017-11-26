## Nome do Programa: Pesquisa de Diretórios
## Autor: Guilherme Mendes
## Descrição: O programa recebe um caminho do usuário e retorna se ele pertence a
## um arquivo ou diretório, caso exista

## Carregar pacotes
import os
import os.path


while True:

    file = str(input("Pesquisa (0 para sair): "))

    if file == "0":
        break

    if os.path.exists(file):
        if os.path.isdir(file):
            print ("Diretório")

        elif os.path.isfile(file):
            print ("Arquivo")
    else:
        print ("Não existe")

    

