import sqlite3

conexao = sqlite3.connect('aula01.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
''')

conexao.commit()

cursor.execute("INSERT INTO contatos (nome, telefone) VALUES ('Johel', '123456')")
cursor.execute("INSERT INTO contatos (nome, telefone) VALUES ('Fulano', '123456')")
conexao.commit()

# Lista todas as linhas no banco de dados
cursor.execute("SELECT * FROM contatos")
contatos = cursor.fetchall()
print("contatos no banco de dados:", contatos)

cursor.execute("DELETE FROM contatos WHERE id = 1")

cursor.execute("SELECT * FROM contatos")
contatos = cursor.fetchall()
print("contatos no banco de dados:", contatos)

conexao.close()

#CRUD - CREATE, READ, UPDATE, DELETE
