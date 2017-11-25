#-------------------------------------------------------
# Exemplo de dicionário com estoque e operações de venda
#-------------------------------------------------------

estoque = {"tomate": [1000, 2.30],
           "alface": [ 500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [ 100, 1.50] }

historico = []

while True:
    produto = str(input("Selecionar produto (E para visualizar estoque, H para visualizar histórico): "))

    if produto == "E":
        print("\nESTOQUE:")
        
        for info in estoque.items():
            nome, dados = info
            print("  {0}: {1: =4} unidades - R${2:5.2f} cada".format(nome, dados[0], dados[1]))

    elif produto == "H":
        print ("\nHISTÓRICO DE VENDAS:")

        if len(historico) > 0:

            total = 0

            for info in historico:
                nome, qnt, valor = info
                total += valor
                print("  {0}: {1: =4} un. por R${2: >8.2f}".format(nome, qnt, valor))

            print("TOTAL ---------------- R${0: >8.2f}".format(total))

        else:
            print("Não há registros")
                
        
    elif produto in estoque:

        qnt = int(input("Quantidade comprada: "))

        if qnt <= 0:
            print("Insira um valor válido")
            
        elif estoque[produto][0] >= qnt:
            
            preço = estoque[produto][1]
            valor = qnt * preço
            estoque[produto][0] -= qnt

            historico.append([produto, qnt, valor])

            print ("\nCompra efetuada com sucesso")
            print ("%s - %d un. por R$%5.2f" % (produto, qnt, valor))
            print ("Restam %d un. de %s no estoque" % (estoque[produto][0], produto))
            
        else:
            print("A quantidade desejada é maior do que a quantidade em estoque")

    else:
        print("Este produto não está disponível no estoque")

    print("\n")
