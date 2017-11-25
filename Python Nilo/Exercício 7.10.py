#-------------------------------------
# Jogo da Velha
#-------------------------------------

grade = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
jogador = 1
win = False

while True:
    symbol = "0" if jogador == 1 else "X"
    print ("É a vez do jogador %s (%s)" % (jogador, symbol))
    
    lin = int(input("Em que linha você deseja jogar? "))
    col = int(input("Em que coluna você deseja jogar? "))

    if lin < 1 or lin > 3 or col < 1 or col > 3:
        print ("Posição inválida")

    elif grade[lin-1][col-1] != 0:
        print ("Esta posição já foi ocupada")

    else:

        grade[lin-1][col-1] = jogador

        print("\n")

        for l in grade:
            text = ""

            c = 0
            while c < len(l):
                text += "| " if c == 1 else " "
                
                if l[c] == 1:
                    text += "0"
                elif l[c] == 2:
                    text += "X"
                else:
                    text += " "

                text += " |" if c == 1 else " "

                c += 1

            print(text)
            print("---+---+---")

        jogador = 3 - jogador
        
        for l in grade:
            count = 0

            for c in l:
                if c == 1:
                    count += 1
                elif c == 2:
                    count -= 1

            if count == 3:
                print("\nJogador 1 venceu!")
                win = True
                break
            elif count == -3:
                print("\nJogador 2 venceu!")
                win = True
                break


        c = 0

        while c < len(l):
            count = 0

            for l in grade:
                if l[c] == 1:
                    count += 1
                elif l[c] == 2:
                    count -= 1

            if count == 3:
                print("\nJogador 1 venceu!")
                win = True
                break
            elif count == -3:
                print("n\Jogador 2 venceu!")
                win = True
                break
            
            c += 1
        
    if win == True:
        break

            
        

    print("\n")

        
