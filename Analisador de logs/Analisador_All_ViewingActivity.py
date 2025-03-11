# O arquivo weblog.csv contém um log de um servidor web no formato:
# IP, data, METODO endereço HTTP/1.1, status

# Seu analisador deve responder perguntas do tipo:
# - Quantas requisições de cada método foram feitas?
# - Quais os IPs que mais acessaram?
# - Quantas requisições com status de erro tiveram?
# Crie suas próprias perguntas.

import csv
import re
from collections import Counter

arquivo = open("Analisador de logs\\All_ViewingActivity.csv", "r", encoding="utf-8")
tabela = csv.reader(arquivo)

global r
r = 's'

def pergunta():
    global r
    r = input("""Deseja realizar outra operação?
              's' para continuar o programa de LOGS
              'n' Para encerrar o programa de LOGS: """)

def contador_de_quantas_requisiçoes_do_player():
    arquivo = open("Analisador de logs\\All_ViewingActivity.csv", "r", encoding="utf-8")
    # COLOCAR \\ PARA NÃO APARECER ERRO:
    # SyntaxWarning: invalid escape sequence
    tabela = csv.reader(arquivo)
    contador_TRAILER = 0
    contador_HOOK = 0
    contador_TEASER_TRAILER = 0
    contador_vazio = 0
    try:
        for linha in tabela:
            if linha[5].startswith("TRAILER"):
                    contador_TRAILER = contador_TRAILER + 1
            elif linha[5].startswith("HOOK"):
                    contador_HOOK = contador_HOOK +1
            elif linha[5].startswith("TEASER_TRAILER"):
                    contador_TEASER_TRAILER = contador_TEASER_TRAILER +1
            else:
                 contador_vazio = contador_vazio + 1
    except IndexError:
         print("end")
    print(f"O player TRAILER foi usado: {contador_TRAILER}")
    print(f"O player HOOK foi usado: {contador_HOOK}")
    print(f"O player TEASER_TRAILER foi usado: {contador_TEASER_TRAILER}")
    pergunta()

def usuario_mais_usados():
    arquivo = open("Analisador de logs\\All_ViewingActivity.csv", "r", encoding="utf-8")
    tabela = csv.reader(arquivo)
    usuarios = []
    try:
        for linha in tabela:
            usuario = linha[0]
            usuarios.append(usuario)
    except IndexError:
         print("")
        
    contador_usuarios = Counter(usuarios) #Modolo Collections Counter ---> Contar frequencia
    usuario_mais_usado = contador_usuarios.most_common(1)[0][0]# O "(1)" representa o elemento mais comum e o "[0]"o indice da lista
    quantidade_usuario_mais_usado = contador_usuarios.most_common(1)[0][1]

    print("Lista de IPs únicos:", list(contador_usuarios.keys()))
    print(f'O IP mais usado é {usuario_mais_usado} e utilizou {quantidade_usuario_mais_usado} vezes.')
    pergunta()

def contar_Tipo_de_Dispositivo():
    with open("Analisador de logs\\All_ViewingActivity.csv", "r", encoding="utf-8") as arquivo:
        tabela = csv.reader(arquivo)
        dispositivos = []
        next(tabela) # Permite pular a primeira linha(nome do atributo)
        for linha in tabela:
            try:
                dispositivos.append(linha[6])
            except IndexError:
                 print("")

        contador_dispositivos = Counter(dispositivos)
        if contador_dispositivos:
            print("\nContagem de status:")
            for dispositivos, quantidade in contador_dispositivos.items():
                print(f"{dispositivos}: {quantidade}")
    pergunta()

def contador_de_atributos():
    arquivo = open("Analisador de logs\\All_ViewingActivity.csv", "r", encoding="utf-8")
    # COLOCAR \\ PARA NÃO APARECER ERRO:
    # SyntaxWarning: invalid escape sequence
    tabela = csv.reader(arquivo)
    contador_NONE = 0
    contador_USER_INTERACTION = 0
    contador_vazio = 0
    try:
        for linha in tabela:
            if linha[3].endswith("Autoplayed: user action: None; "):
                    contador_NONE = contador_NONE + 1
            elif linha[3].startswith("Autoplayed: user action: User_Interaction; "):
                    contador_USER_INTERACTION = contador_USER_INTERACTION +1
            else:
                 contador_vazio = contador_vazio + 1
    except IndexError:
         print("end")
    print(f"O player tocou automaticamente: {contador_NONE}")
    print(f"O usuario começou a rodar: {contador_USER_INTERACTION}")
    pergunta()

def menu():
    while r == 's':
        print("============ Manipulação de LOGS ============")
        print("1 - Quantidade De Requisições De Cada Player")
        print("2 - Usuario Mais Usados")
        print("3 - Contador de Tipos De Dispositivos")
        print("4 - Contador de Atributos")
        opção = input("Informe o numero da operação que deseja: ")
        if opção == "1":
            print("================ Quantidade De Requisições De Cada Player =================")
            contador_de_quantas_requisiçoes_do_player()
            print("===========================================================================")
        elif opção == "2":
            print("============================ Usuario Mais Usado =============================")
            usuario_mais_usados()
            print("===========================================================================")
        elif opção == "3":
            print("============================ Contador de Tipos De Dispositivos ===========================")
            contar_Tipo_de_Dispositivo()
            print("===========================================================================")
        elif opção == "4":
            print("============================ Contador de Tipos De Dispositivos ===========================")
            contador_de_atributos()
            print("===========================================================================")
        
        


menu()
print("Programa de LOGS encerrada!")