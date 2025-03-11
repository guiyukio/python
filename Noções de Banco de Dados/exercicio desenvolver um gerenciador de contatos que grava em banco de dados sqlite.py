import sqlite3

global cursor
global agenda
global opção

opção = "n"

agenda = sqlite3.connect('Noções de Banco de Dados\\primeira aula\\gerenciador de agenda contatos.db')
cursor = agenda.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
''')

agenda.commit()

# cursor.execute("INSERT INTO contatos (nome, telefone) VALUES ('Johel', '123456')")
# cursor.execute("INSERT INTO contatos (nome, telefone) VALUES ('Fulano', '123456')")
# agenda.commit()


def adicionar_contato():
    global cursor
    global agenda
    nome = input("Insira o contato com nome: ")
    numero = input("Insira o numero da pessoa: ")
    agenda.commit()
    cursor.execute(f"INSERT INTO contatos (nome, telefone) VALUES (?,?)",(nome,numero))
    print(f"Contato adicionado com sucesso!!!")


def listar_contatos():
    global cursor
    global agenda
    print("============== Contatos ==============")
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    print("contatos no banco de dados:", contatos)

def buscar_contato():
    global cursor
    global agenda
    buscar = int(input("Insira o nome que deseja buscar: "))
    agenda.commit()
    cursor.execute(f"SELECT nome, telefone FROM contatos WHERE id = {buscar}")
    resultados = cursor.fetchall()
    print("contatos no banco de dados que vieram da pesquisa:", resultados)

def editar_contato():
    global cursor
    global agenda
    agenda.commit()
    print("=============================== EDITAR CONTATO ================================")
    id_do_contato_editar = int(input("Informe o id do contato a ser editado: "))
    editar = input("Qual parte deseja alterar do contato: ")
    if editar not in ("nome", "telefone"):
        print("Campo inválido. Digite 'nome' ou 'telefone'.")
        return
    novo_valor = input(f"Digite o novo valor para {editar}: ")
    cursor.execute(f"UPDATE contatos SET {editar} = ? WHERE id = ?", (novo_valor, id_do_contato_editar))
    agenda.commit()

def remover_contato():
    global cursor
    global agenda
    agenda.commit()
    remover = int(input("Informe ID do contato que deseja remover: "))
    cursor.execute(f"DELETE FROM contatos WHERE id = {remover}")
    print(f'O contato foi removido')

while opção != "S" or opção != 's':
    print("============ Agenda de Contatos ============")
    print("1 - Adicionar Contatos")
    print("2 - Listar Contatos")
    print("3 - Buscar Contatos")
    print("4 - Editar contato")
    print("5 - Remover contatos")
    print("s - Para encerrar a Agenda de Contatos")
    opção = input("Informe o numero da operação que deseja!!! ")
    if opção == "1":
        adicionar_contato()
    elif opção == "2":
        listar_contatos()
    elif opção == "3":
        buscar_contato()
    elif opção == "4":
        editar_contato()
    elif opção == "5":
        remover_contato()
    elif opção == 's':
        break
print("Agenda de contatos encerrada!")

agenda.close()