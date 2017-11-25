import sqlite3
from contextlib import closing

produtos = [ ("Maçã", 4),
             ("Pêra", 6),
             ("Bolo", 9)]

with sqlite3.connect("produtos.db") as conexão:
    with closing(conexão.cursor()) as cursor:

        cursor.executemany('''

insert into produtos(nome, preço) values(?, ?)

''', produtos)

        conexão.commit()
