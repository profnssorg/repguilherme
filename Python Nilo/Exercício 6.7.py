#----------------------------------------------------------------
# Verifica se expressões com parênteses possuem a sintaxe correta
#----------------------------------------------------------------

while True:

    exp = list(input("Expressão (0 para sair): "))

    if exp == ["0"]:
        break
    
    new = []
    error = False

    for p in exp:
        if p == "(":
            new.append(p)
        elif p == ")":
            if len(new) == 0:
                error = True
                break
            else:
                new.pop(-1)

    if len(new) != 0 or error == True:
        print("A expressão contém um erro.")
    else:
        print("A expressão está OK!")

    print("\n")
