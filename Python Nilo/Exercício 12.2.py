import sqlite3
from contextlib import closing

nome = input("Nome: ")
npre = input("Novo preço: ")

with sqlite3.connect("produtos.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("""update produtos set preço = ? where nome = ?""", (npre, nome))
        conexão.commit()

        
        cursor.execute("select * from produtos")

        while True:
            resultado = cursor.fetchone()

            if resultado == None:
                break
            print("Produto: %s\nPreço: %s\n" % resultado)
