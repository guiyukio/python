#PARTE 1

#Exercício 1:
# ● Crie um arquivo chamado "meu_arquivo.txt".
# ● Escreva as frases "Olá, mundo!" e "Aprendendo Python!" no arquivo.
# ● Leia o arquivo e imprima o conteúdo no console.

# with open('manipulação de arquivos\\meu_arquivo.txt', 'w') as arquivo:
#     arquivo = open('manipulação de arquivos\\meu_arquivo.txt','w')
#CRIAÇÃO DO ARQUIVO

# with open('manipulação de arquivos\\meu_arquivo.txt','w') as arquivo:
#     arquivo.writelines(["Olá, mundo!\n", "Aprendendo Python 2\n"])
# ESCREVENDO NO ARQUIVO

# with open('manipulação de arquivos\\meu_arquivo.txt','r') as arquivo:
#     print(arquivo.read())
# LENDO E PRINTANDO O ARQUIVO

# 1) Contar palavras: Leia o conteúdo de um arquivo e conte o número total 
# de palavras

# with open('manipulação de arquivos\\copia.txt','r') as arquivo:
#     conteudo = arquivo.read()
#     contador = 0
#     for palavra in conteudo.split(' '):
#         contador = contador + 1
    
# print(contador + 1)

# 2) Número de linhas: Crie um script que conta e exibe o número total de 
# linhas em um arquivo

# with open('manipulação de arquivos\\meu_arquivo.txt', 'r') as arquivo:
#     x = len(arquivo.readlines())
#     print(x)

# 3) Copia e cola: Leia um arquivo e copie seu conteúdo para 
# outro arquivo chamado copia.txt.

# with open('manipulação de arquivos\\copia.txt', 'w') as arquivo:
#     arquivo = open('manipulação de arquivos\\copia.txt','w')

# with open('manipulação de arquivos\\meu_arquivo.txt','r') as arquivo:
#     conteudo = arquivo.read()

# with open('manipulação de arquivos\\copia.txt', 'a') as arquivo:
#     arquivo.writelines(conteudo)


# with open('manipulação de arquivos\\copia.txt','r') as arquivo:
#     print(arquivo.read())

# 4) Busca em arquivos: Leia um arquivo e procure por uma palavra específica.
# Exiba as linhas onde a palavra aparece.

# with open('manipulação de arquivos\\meu_arquivo.txt','r') as arquivo:
#       for num, linha in enumerate(arquivo.readlines()):
#             if 'Python' in linha:
#                   print(f'palavra Python encontrada na linha: {num + 1}')
        


# 5) Ordenar palavras: Leia o conteúdo de um arquivo, extraia todas as 
# palavras, e salve-as em ordem alfabética em um novo arquivo.



# 6) Remoção de linhas vazias: Leia um arquivo e crie outro arquivo 
# sem linhas em branco.



# 7) Estatísticas do texto: Leia um arquivo e exiba:
# ● O número total de caracteres.
# ● O número de palavras.
# ● O número de linhas

# with open('manipulação de arquivos\\meu_arquivo.txt','r') as arquivo:
#     conteudo = arquivo.read()
#     contador = 0
#     lista = conteudo.split(' ')
#     for caracter in conteudo:
#             if caracter.isalnum:
#                 contador = contador + 1
# print(f'O numero de caracteres é: {contador}')
# # ● O número total de caracteres.

# with open('manipulação de arquivos\\meu_arquivo.txt','r') as arquivo:
#     conteudo = arquivo.read()
#     word = len(lista)
# print(f'O numero de palavras é: {word}')
# # ● O número de palavras.

# with open('manipulação de arquivos\\meu_arquivo.txt', 'r') as arquivo:
#     x = len(arquivo.readlines())
#     print(f'O numero de linhas é: {x}')
# # ● O número de linhas

# print(lista)


#PARTE 2

# 1) Criar e Ler um CSV: Crie um arquivo CSV chamado alunos.csv com os dados de 3 alunos 
# (Nome, Idade, Nota). Em seguida, leia e exiba o conteúdo no console.

# with open('manipulação de arquivos\\alunos.csv', 'w') as arquivo:
#     arquivo = open('manipulação de arquivos\\alunos.csv','w')

# with open('manipulação de arquivos\\alunos.csv','a') as arquivo:
#     arquivo.writelines([f"'nome': 'Guilherme' \n", 
#                         f"'idade': 25 \n", 
#                         f"'nota': 9 \n",
#                         f"''\n",
#                         f"'nome': 'Fulano' \n", 
#                         f"'idade': 30 \n", 
#                         f"'nota': 10 \n",
#                         f"''\n",
#                         f"'nome': 'Ciclano' \n", 
#                         f"'idade': 28 \n", 
#                         f"'nota': 7 \n",
#                         f"''\n"
#                         ])

# alunos = open('manipulação de arquivos\\alunos.csv','r')

# with open('manipulação de arquivos\\alunos.csv','r') as arquivo:
#     print(arquivo.read())

# 2) Converter Dicionário em JSON: Converta o dicionário { "nome": "Maria", "idade": 25 }
# em JSON e salve no arquivo dados.json

# import json

# dicionario = { "nome": "Maria", "idade": 25 }

# with open("manipulação de arquivos\\dados.json", "w") as arquivo:
#  json.dump(dicionario, arquivo)


# Desafio 1
# Configuração de Aplicação:
# ● Crie um arquivo JSON chamado config.json que contenha configurações fictícias de 
# um sistema (ex.: tema, idioma, permissões).
# ● Escreva um programa que permita alterar uma configuração e salve novamente o 
# arquivo com as alterações

# import json

# configurações = {"Tema" : "Escuro", "Idioma" : "PT-BR","Permissões" : "GPS"}

# with open("manipulação de arquivos\\config.json","w") as arquivo:
#     json.dump(configurações,arquivo)

# with open("manipulação de arquivos\\config.json","r") as arquivo:
#     config = json.load(arquivo)
#     # print(config["Tema"])

# r = 's'

# def alterar():
#     alter = input("Informe a configuração que deseja alterar: ")
#     valor = input("Informe o valor da alteração: ")
#     for configuração in configurações:
#         if configuração.startswith(alter):
#             configurações[alter] = valor
#             print("Valor alterado")
#             with open("manipulação de arquivos\\config.json","w") as arquivo:
#                 json.dump(configurações, arquivo)
#     with open("manipulação de arquivos\\config.json","r") as arquivo:
#         config = json.load(arquivo)
#         print(config)

# alterar()

# Desafio 2
# Agenda de contatos:
# Escreva um programa que permita adicionar, editar ou remover contatos
# de uma agenda de contatos. 
# Seu programa deve utilizar um arquivo JSON para persistir os dados

# import json

# agenda_de_contatos = open("manipulação de arquivos\\agenda_de_contatos.json","r")

# with open('manipulação de arquivos\\agenda_de_contatos.json', 'w') as arquivo:
#     arquivo = open('manipulação de arquivos\\agenda_de_contatos.json','w')

# with open("manipulação de arquivos\\agenda_de_contatos.json","w") as arquivo:
#     json.dump(agenda_de_contatos,arquivo)

# global r
# r = 'n'

# with open("manipulação de arquivos\\agenda_de_contatos.json","r") as arquivo:
#     agenda = json.load(arquivo)
#     print(agenda)

# def adicionar_contato(nome,numero):
#     contato = {nome : numero}
#     agenda.update(contato)
#     print(f"Contato adicionado com sucesso!!!")

#     with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#         json.dump(agenda, arquivo)

# def listar_contatos():
#     print("============== Contatos ==============")
#     for contato in agenda:
#         valor = agenda[contato]
#         print(f' - {contato} - {valor}')

# def buscar_contato():
#     busca = input("Insira o nome que deseja buscar: ")
#     for contato in agenda:
#         if contato == busca:
#             valor = agenda[contato]
#     resultados = [contato for contato in agenda if contato.startswith(busca)]#Busca e Guarda todos os resultados que começam com busca!
#     print(f'O contato que tem o elemento começado com {busca} : {resultados} - {valor}')

# def editar_contato(editar):
#         novo_numero = input("Informe o novo numero do contato: ")
#         agenda[editar] = novo_numero

#         with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#             json.dump(agenda, arquivo)

# def remover_contato():
#     remover = input("Informe o contato que deseja remover: ")
#     del agenda[remover]
#     print(f'O contato {remover} foi removido')

#     with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#         json.dump(agenda, arquivo)

# while r != "S" or r != 's':
#     print("============ Agenda de Contatos ============")
#     print("1 - Adicionar Contatos")
#     print("2 - Listar Contatos")
#     print("3 - Buscar Contatos")
#     print("4 - Editar contato")
#     print("5 - Remover contatos")
#     print("s - Para encerrar a Agenda de Contatos")
#     r = input("Informe o numero da operação que deseja!!! ")
#     if r == "1":
#         nome = input("Insira o contato com nome: ")
#         numero = input("Insira o numero da pessoa: ")
#         adicionar_contato(nome,numero)
#         r = input("""Deseja encerrar a Agenda de Contatos? 
#               Clique 's' para encerrar a agenda!""")
#     elif r == "2":
#         listar_contatos()
#         r = input("""Deseja encerrar a Agenda de Contatos? 
#               Clique 's' para encerrar a agenda!""")
#     elif r == "3":
#         buscar_contato()
#         r = input("""Deseja encerrar a Agenda de Contatos? 
#               Clique 's' para encerrar a agenda!""")
#     elif r == "4":
#         editar = input("Informe o contato que deseja editar: ")
#         editar_contato(editar)
#         r = input("""Deseja encerrar a Agenda de Contatos? 
#               Clique 's' para encerrar a agenda!""")
#     elif r == "5":
#         remover_contato()
#         r = input("""Deseja encerrar a Agenda de Contatos? 
#               Clique 's' para encerrar a agenda!""")
#     elif r == 's':
#         break
# print("Agenda de contatos encerrada!")


# Desafio 3
# Desafio 1 + Desafio 2

# with open('manipulação de arquivos\\Agenda_de_contatos.json', 'w') as arquivo:
#     arquivo = open('manipulação de arquivos\\Agenda_de_contatos.json','w')

# with open('manipulação de arquivos\\Agenda_de_contatos.json','r') as arquivo:
#     print(arquivo.read())

# import json

# r = 'n'

# agenda_de_contatos = open("manipulação de arquivos\\agenda_de_contatos.json","r")

# with open('manipulação de arquivos\\agenda_de_contatos.json', 'w') as arquivo:
#     arquivo = open('manipulação de arquivos\\agenda_de_contatos.json','w')

# with open("manipulação de arquivos\\agenda_de_contatos.json","w") as arquivo:
#     json.dump(agenda_de_contatos,arquivo)

# with open("manipulação de arquivos\\agenda_de_contatos.json","r") as arquivo:
#     agenda = json.load(arquivo)
#     print(agenda)

# def resposta():
#     r = input("""Deseja encerrar a Agenda de Contatos? 
#               Clique 's' para encerrar a agenda!""")

# def adicionar_contato(nome,numero):
#     contato = {nome : numero}
#     agenda.update(contato)
#     print(f"Contato adicionado com sucesso!!!")

#     with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#         json.dump(agenda, arquivo)
#         resposta()

# def listar_contatos():
#     print("============== Contatos ==============")
#     for contato in agenda:
#         valor = agenda[contato]
#         print(f' - {contato} - {valor}')
    
#     resposta()

# def buscar_contato():
#     busca = input("Insira o nome que deseja buscar: ")
#     for contato in agenda:
#         if contato == busca:
#             valor = agenda[contato]
#     resultados = [contato for contato in agenda if contato.startswith(busca)]#Busca e Guarda todos os resultados que começam com busca!
#     print(f'O contato que tem o elemento começado com {busca} : {resultados} - {valor}')
#     resposta()

# def editar_contato(editar):
#         novo_numero = input("Informe o novo numero do contato: ")
#         agenda[editar] = novo_numero

#         with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#             json.dump(agenda, arquivo)
        
#         resposta()

# def remover_contato():
#     remover = input("Informe o contato que deseja remover: ")
#     del agenda[remover]
#     print(f'O contato {remover} foi removido')

#     with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#         json.dump(agenda, arquivo)
    
#     resposta()

# def answer():
#     r = input("""Wish to close the Contact Book?
#               "S" to close!""")

# def Add_contact(nome,numero):
#     contato = {nome : numero}
#     agenda.update(contato)
#     print(f"Contect succefull addition!!!")

#     with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#         json.dump(agenda, arquivo)
#         resposta()

# def list_contact():
#     print("============== Contacts ==============")
#     for contato in agenda:
#         valor = agenda[contato]
#         print(f' - {contato} - {valor}')
    
#     resposta()

# def serch_contact():
#     busca = input("Insert the name you wish to serch: ")
#     for contato in agenda:
#         if contato == busca:
#             valor = agenda[contato]
#     resultados = [contato for contato in agenda if contato.startswith(busca)]#Busca e Guarda todos os resultados que começam com busca!
#     print(f'{resultados} - {valor}')
#     resposta()

# def edit_contact(editar):
#         novo_numero = input("Inform the new number: ")
#         agenda[editar] = novo_numero

#         with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#             json.dump(agenda, arquivo)
        
#         resposta()

# def remove_contact():
#     remover = input("Inform the name you wish to remove: ")
#     del agenda[remover]
#     print(f'The Contact: {remover} Removed Succefully')

#     with open("manipulação de arquivos\\agenda_de_contatos.json", "w") as arquivo:
#         json.dump(agenda, arquivo)
    
#     resposta()

# with open("manipulação de arquivos\\config.json","w") as arquivo:
#     json.dump(configurações,arquivo)

# with open("manipulação de arquivos\\config.json","r") as arquivo:
#     config = json.load(arquivo)
#     configurações = config


# def alterar_configuração():
#     alter = input("Informe a configuração que deseja alterar: ")
#     valor = input("Informe o valor da alteração: ")
#     for configuração in configurações:
#         if configuração.startswith(alter):
#             configurações[alter] = valor
#             print("Valor alterado")
#             with open("manipulação de arquivos\\config.json","w") as arquivo:
#                 json.dump(configurações, arquivo)
#     with open("manipulação de arquivos\\config.json","r") as arquivo:
#         config = json.load(arquivo)
#         print(config)

# def settings():
#     alter = input("Inform the configuration you want to change: ")
#     valor = input("Inform the new value: ")
#     for configuração in configurações:
#         if configuração.startswith(alter):
#             configurações[alter] = valor
#             print("Value Changed")
#             with open("manipulação de arquivos\\config.json","w") as arquivo:
#                 json.dump(configurações, arquivo)
#     with open("manipulação de arquivos\\config.json","r") as arquivo:
#         config = json.load(arquivo)
#         print(config)

# def menu_PTBR():
#     print("============ Agenda de Contatos ============")
#     print("1 - Adicionar Contatos")
#     print("2 - Listar Contatos")
#     print("3 - Buscar Contatos")
#     print("4 - Editar contato")
#     print("5 - Remover contatos")
#     print("6 - Configurações")
#     opção = input("Informe o numero da operação que deseja: ")
#     if opção == "1":
#         nome = input("Insira o contato com nome: ")
#         numero = input("Insira o numero da pessoa: ")
#         adicionar_contato(nome,numero)
#     elif opção == "2":
#         listar_contatos()
#     elif opção == "3":
#         buscar_contato()
#     elif opção == "4":
#         editar = input("Informe o contato que deseja editar: ")
#         editar_contato(editar)
#     elif opção == "5":
#         remover_contato()
#     elif opção == "6":
#         print(config)
#         alterar_configuração()
# print("Agenda de contatos encerrada!")

# def menu_EN():
#     print("============ Contact Book ============")
#     print("1 - Add Contact")
#     print("2 - List contacts")
#     print("3 - Serch Contatos")
#     print("4 - Edit contato")
#     print("5 - Remove contatos")
#     print("6 - Settings")
#     opção = input("Inform the number of the operation you want to use: ")
#     if opção == "1":
#         nome = input("Insert the name of the new contact: ")
#         numero = input("Insert the number of the new contact: ")
#         Add_contact(nome,numero)
#     elif opção == "2":
#         list_contact()
#     elif opção == "3":
#         serch_contact()
#     elif opção == "4":
#         editar = input("Informe o contato que deseja editar: ")
#         edit_contact(editar)
#     elif opção == "5":
#         remove_contact()
#     elif opção == "6":
#         print(config)
#         settings()
# print("Closing Contact Book")

# while r == 'n':
#     if config["Idioma"] == "PT-BR":
#         menu_PTBR()
#     elif config["Idioma"] == "EN":
#         menu_EN()


# 1. Criar um arquivo Word
# ● Crie um programa que:
# ○ Gera um arquivo Word chamado documento.docx.
# ○ Adiciona um título em negrito e sublinhado.
# ○ Adiciona dois parágrafos de texto.
# ○ Salva o arquivo.

# from docx import Document

# doc = Document()
# head = doc.add_heading("Primeiro exercicio",1)
# head.add_run('underline').underline = True
# head.add_run('bold').bold = True
# p1 = doc.add_paragraph("Primeiro paragrafo")
# p1.add_run('bold').bold = True
# p1.add_run('underline').font.underline = True
# p2 = doc.add_paragraph("Segundo paragrafo")
# p2.add_run('bold').bold = True
# p2.add_run('underline').font.underline = True
# doc.save("manipulação de arquivos\\documento.docx")

# from docx import Document

# doc = Document("manipulação de arquivos\\documento.docx")
# for paragraph in doc.paragraphs:
#     print(paragraph.text)

# 2. Ler o conteúdo de um arquivo Word
# ● Crie um programa que:
# ○ Abra um arquivo Word existente (texto.docx).
# ○ Leia o conteúdo de todos os parágrafos e exiba no terminal.


# from docx import Document

# doc = Document("manipulação de arquivos\\documento.docx")
# for paragraph in doc.paragraphs:
#     print(paragraph.text)

# 3. Contar palavras em um arquivo Word
# ● Crie um programa que:
# ○ Leia um arquivo Word (documento.docx).
# ○ Conte o número total de palavras no arquivo.
# ○ Exiba o resultado no terminal.

# from docx import Document


# doc = Document("manipulação de arquivos\\documento.docx")
# for paragraph in doc.paragraphs:
#     print(paragraph.text)
#     conteudo = (paragraph.text)
#     lista = conteudo.split(" ")
#     palavra = len(lista)
#     print(palavra)

# 4. Adicionar uma tabela em um arquivo Word
# ● Crie um programa que:
# ○ Gere um arquivo Word chamado tabela.docx.
# ○ Insira uma tabela com 3 colunas e 5 linhas.
# ○ Preencha as células com valores como "Linha X, Coluna Y".
# ○ Salve o arquivo

# from docx import Document

# doc = Document()
# table = doc.add_table(rows=5, cols=3)
# table.cell(0, 0).text = "Linha 1, Coluna 1"
# table.cell(0, 1).text = "Linha 1, Coluna 2"
# table.cell(0, 2).text = "Linha 1, Coluna 3"
# table.cell(1, 0).text = "Linha 2, Coluna 1"
# table.cell(1, 1).text = "Linha 2, Coluna 2"
# table.cell(1, 2).text = "Linha 2, Coluna 3"
# table.cell(2, 0).text = "Linha 3, Coluna 1"
# table.cell(2, 1).text = "Linha 3, Coluna 2"
# table.cell(2, 2).text = "Linha 3, Coluna 3"
# table.cell(3, 0).text = "Linha 4, Coluna 1"
# table.cell(3, 1).text = "Linha 4, Coluna 2"
# table.cell(3, 2).text = "Linha 4, Coluna 3"
# table.cell(4, 0).text = "Linha 5, Coluna 1"
# table.cell(4, 1).text = "Linha 5, Coluna 2"
# table.cell(4, 2).text = "Linha 5, Coluna 3"
# doc.save('manipulação de arquivos\\tabela.docx')


# 5. Substituir palavras em um arquivo Word
# ● Crie um programa que:
# ○ Leia um arquivo Word existente.
# ○ Substitua todas as ocorrências de uma palavra específica (ex.: "Python") por
# outra palavra (ex.: "Elixir").
# ○ Salve o resultado em um novo arquivo.


# from docx import Document


# doc = Document()
# p1 = doc.add_paragraph("Exercícios com arquivos Excel")
# doc.save("Exercicio5_word.docx")

# doc = Document("manipulação de arquivos\\Exercicio5_word.docx")
# for paragraph in doc.paragraphs:
#     conteudo = (paragraph.text)
#     lista = [conteudo.split(" ")]

# for palavra in lista:
#     if palavra == "Excel":
#         lista[palavra] = 'word'

# print(lista)

# Exercícios com arquivos Excel (.xlsx)

# 6. Criar uma planilha com dados fictícios
# ● Crie um programa que:
# ○ Gere um arquivo Excel chamado dados.xlsx.
# ○ Crie uma planilha chamada "Vendas".
# ○ Adicione cabeçalhos nas colunas (ex.: "Produto", "Quantidade", "Preço").
# ○ Adicione 5 linhas de dados fictícios.
# ○ Salve o arquivo.

# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# ws.title = "Vendas"
# ws.append(['Produto', 'Quantidade', 'Preço'])
# ws.append(['Feijão', 30, 170.50])
# ws.append(['Arroz', 25, 150.50])
# ws.append(['Banana', 33, 70.50])
# ws.append(['Açucar', 27, 120.50])
# ws.append(['Laranja', 42, 80.50])
# wb.save('dados.xlsx')

# Alterei os valores para acomodar o outro exercicio

# 7. Ler e exibir dados de uma planilha
# ● Crie um programa que:
# ○ Abra o arquivo Excel dados.xlsx.
# ○ Leia os dados da planilha "Vendas".
# ○ Exiba no terminal o conteúdo de todas as células.

# from openpyxl import load_workbook
# wb = load_workbook('manipulação de arquivos\\dados.xlsx')
# ws = wb.active
# for row in ws.iter_rows(values_only=True):
#    print(row)

# 8. Filtrar dados em uma planilha
# ● Crie um programa que:
# ○ Leia uma planilha Excel contendo dados de vendas.
# ○ Filtre as linhas onde o valor total seja maior que R$ 100,00.
# ○ Salve essas linhas em uma nova planilha chamada vendas_filtradas.xlsx.
# Integração Word e Excel

# import openpyxl

# from openpyxl import load_workbook

# planilha = openpyxl.load_workbook("manipulação de arquivos\\dados.xlsx")
# tabela = planilha.active
# nova_planilha = openpyxl.Workbook()
# nova_tabela = nova_planilha.active
# nova_tabela.append([cell.value for cell in tabela[1]])
# for row in tabela.iter_rows(min_row=2):
#     valor_total = row[2].value
#     if valor_total > 100:
#         nova_tabela.append([cell.value for cell in row])
# nova_planilha.save("vendas_filtradas.xlsx")

# print("Planilha filtrada e salva com sucesso!")

# Para abrir a nova tabela seguir esse comando
# workbook = openpyxl.load_workbook("vendas_filtradas.xlsx")
# sheet = workbook.active
# for row in sheet.iter_rows():
#     print([cell.value for cell in row])


# 9. Gerar relatórios em Word a partir de Excel
# ● Crie um programa que:
# ○ Leia uma planilha Excel com dados (ex.: "Nome do Cliente", "Valor da Compra").
# ○ Crie um arquivo Word chamado relatorio.docx.
# ○ Adicione os dados do Excel no Word, formatados em forma de tabela

# import openpyxl
# from openpyxl import Workbook
# from openpyxl import load_workbook
# from docx import Document
# from docx import *

# doc = Document()
# doc.save("manipulação de arquivos\\documento.docx")

# planilha = openpyxl.load_workbook("manipulação de arquivos\\Relatorio EX 9 Manipulação de dados.xlsx")
# tabela = planilha.active
# nova_planilha = openpyxl.Workbook()
# nova_tabela = nova_planilha.active
# nova_tabela.append([cell.value for cell in tabela[1]])
# for row in tabela.iter_rows(min_row=2):
#     print(row)
#     nova_tabela.append([cell.value for cell in row])

# nova_planilha.save("manipulação de arquivos\\nova_tabela.xlsx")

# print(nova_tabela)

# workbook = openpyxl.load_workbook("manipulação de arquivos\\nova_tabela.xlsx")
# sheet = workbook.active
# for row in sheet.iter_rows():
#     dados = ([cell.value for cell in row])
#     table = doc.add_table(rows=1, cols=2)
#     table.cell(0,0).text = dados

# doc.save('manipulação de arquivos\\relatorio.docx')