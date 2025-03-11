# alunos = open("alunos.txt",'r')

# r ='s'

# def resposta():
#     r = input("Deseja realizar outra operação na Agenda de Contatos? ")

# def adicionar_aluno():
#     novo_aluno = {
#     'nome': input("Nome do aluno: "),
#     'matrícula': input("Numero de matricula: "),
#     'idade': int(input("Informe a idade do aluno: ")),
#     'curso': input("Informe o curso do aluno: ")
#     }
#     alunos.append(novo_aluno)
#     print(f"Aluno adicionado com sucesso!!!")

#     with open('alunos.txt','a') as arquivo:
#         arquivo.writelines(["''\n",
#                         f"'nome': {novo_aluno['nome']}\n",
#                         f"'matrícula':  {novo_aluno['matrícula']}\n", 
#                         f"'idade': {novo_aluno['idade']}\n", 
#                         f"'curso': {novo_aluno['curso']}\n"])

# def listar_alunos():
#     print("============== ALUNOS ==============")
#     for aluno in alunos:
#         print(f' - {aluno}')

# def buscar_aluno():
#     busca = input("Insira o aluno que deseja buscar: ")
#     resultado = {}
#     for aluno in alunos:
#         if aluno == busca:
#             resultado = aluno
#     print(f'Os alunos que começam com: {busca} são: {resultado}')

# def alterar_aluno():
#     alter = input("Informe o aluno que deseja modificar o cadastro: ")
#     campo = input("Informe o campo que deseja alterar: ")
#     valor = input("Informe o valor da alteração: ")
#     for aluno in alunos:
#         if aluno.startswith(alter):
#             print("Valor alterado")
#             with open("config.json","w") as arquivo:
#                 json.dump(configurações, arquivo)
#     with open("config.json","r") as arquivo:
#         config = json.load(arquivo)
#         print(config)

# while r == 's':
#     print("============ CADASTRO ALUNOS ============")
#     print("1 - Adicionar Aluno")
#     print("2 - Listar Aluno")
#     print("3 - Buscar Aluno")
#     print("4 - Alterar Dados de um Aluno")
#     print("S - Sair")
#     opção = input("Informe o numero da operação que deseja!!! ")
#     if opção == "1":
#         adicionar_aluno()
#         resposta()
#     elif opção == "2":
#         listar_alunos()
#         resposta()
#     elif opção == "3":
#         buscar_aluno()
#         resposta()
#     elif opção == "4":
#         alterar_aluno()
#         resposta()
# print("LISTA DE ALUNOS encerrada!")