import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()

cursor.execute("""update agenda set telefone = '123-456' where nome = 'Nilo'""")

conexão.commit()
cursor.close()
conexão.close()
