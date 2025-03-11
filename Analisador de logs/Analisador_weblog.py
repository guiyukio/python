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

arquivo = open("Analisador de logs\\weblog.csv","r")
tabela = csv.reader(arquivo)

global r
r = 's'

def pergunta():
    global r
    r = input("""Deseja realizar outra operação?
              's' para continuar o programa de LOGS
              'n' Para encerrar o programa de LOGS: """)

def contador_de_quantas_requisiçoes_do_metodos():
    arquivo = open("Analisador de logs\\weblog.csv","r")
    # COLOCAR \\ PARA NÃO APARECER ERRO:
    # SyntaxWarning: invalid escape sequence
    tabela = csv.reader(arquivo)
    contador_POST = 0
    contador_GET = 0
    contador_erro = 0
    try:
        for linha in tabela:
            if linha[2].startswith("POST"):
                    contador_POST = contador_POST + 1
            elif linha[2].startswith("GET"):
                    contador_GET = contador_GET +1
            else:
                    contador_erro = contador_erro + 1
    except IndexError:
         print("end")
    print(f"O metodo POST foi usado: {contador_POST}")
    print(f"O metodo GET foi usado: {contador_GET}")
    pergunta()

def contador_de_erros():
    arquivo = open("Analisador de logs\\weblog.csv","r")
    # COLOCAR \\ PARA NÃO APARECER ERRO:
    # SyntaxWarning: invalid escape sequence
    tabela = csv.reader(arquivo)
    contador_POST = 0
    contador_GET = 0
    contador_erro = 0
    try:
        for linha in tabela:
            if linha[2].startswith("POST"):
                    contador_POST = contador_POST + 1
            elif linha[2].startswith("GET"):
                    contador_GET = contador_GET +1
            else:
                    contador_erro = contador_erro + 1
    except IndexError:
         print("end")
    print(f"Quantidade de erros: {contador_erro}")
    pergunta()

def ips_mais_usados():
    with open("Analisador de logs\\weblog.csv", "r") as arquivo:
        tabela = csv.reader(arquivo)
        ips = []
        try:
            for linha in tabela:
                ip = linha[0]
                if re.match(r"^\d{1,9}\.\d{1,9}\.\d{1,9}\.\d{1,9}$", ip):#Verifica se o ip é valido(conjuntos de numeros separados por .)
                    ips.append(ip)
        except IndexError:
             print("")
        
        contador_ips = Counter(ips) # Modolo Collections Counter ---> Contar frequencia
        ip_mais_usado = contador_ips.most_common(1)[0][0]# O "(1)" representa o elemento mais comum e o "[0]"o indice da lista
        quantidade_ip_mais_usado = contador_ips.most_common(1)[0][1]

        print("Lista de IPs únicos:", list(contador_ips.keys()))
        print(f'O IP mais usado é {ip_mais_usado} e apareceu {quantidade_ip_mais_usado} vezes.')
    pergunta()

def contar_status():
    with open("Analisador de logs\\weblog.csv", "r") as arquivo:
        tabela = csv.reader(arquivo)
        status = []
        next(tabela) # Permite pular a primeira linha(nome do atributo)
        for linha in tabela:
            try:
                status.append(linha[3])
            except IndexError:
                 print("")

        contador_status = Counter(status)
        if contador_status:
            print("\nContagem de status:")
            for status, quantidade in contador_status.items():
                print(f"{status}: {quantidade}")
    pergunta()


def menu():
    while r == 's':
        print("============ Manipulação de LOGS ============")
        print("1 - Quantidade De Requisições De Cada Método")
        print("2 - IP's Mais Usados")
        print("3 - Quantidade De Erros")
        print("4 - Contador de Status")
        opção = input("Informe o numero da operação que deseja: ")
        if opção == "1":
            print("================ Quantidade De Requisições De Cada Método =================")
            contador_de_quantas_requisiçoes_do_metodos()
            print("===========================================================================")
        elif opção == "2":
            print("============================ IP's Mais Usados =============================")
            ips_mais_usados()
            print("===========================================================================")
        elif opção == "3":
            print("=========================== Quantidade De ERROS ===========================")
            contador_de_erros()
            print("===========================================================================")
        elif opção == "4":
            print("============================ Contador de Status ===========================")
            contar_status()
            print("===========================================================================")


menu()
print("Programa de LOGS encerrada!")