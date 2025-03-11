# Objetivo:
# Os alunos deverão desenvolver e apresentar um sistema completo, combinando gestão via
# terminal e atendimento automatizado via bot no Telegram. O projeto deve gravar os dados
# em CSV ou JSON para armazenar informações e permitir a interação entre a área do gestor e
# o atendimento ao cliente.
# Escolha um dos seguintes sistemas para desenvolver:

# 1. Sistema de Controle de Pedidos para Restaurantes

# ● Área do Gestor (terminal):
# ○ Cadastrar pratos e atualizar preços.
# ○ Gerenciar pedidos e status (em preparo, pronto, entregue).
# ○ Emitir relatórios de vendas.

# ● Bot no Telegram:
# ○ Ver cardápio e fazer pedidos.
# ○ Acompanhar status do pedido.
# ○ Avaliar o atendimento.

# ● Notificações por E-mail:
# ○ Confirmação de pedido e tempo estimado de entrega.
# ○ Relatórios de vendas diárias para o restaurante.
# ○ Promoções especiais para clientes.


# Requisitos do Trabalho:
# ● Área do Gestor deve ser uma aplicação no terminal, permitindo o gerenciamento do
# sistema.
# ● Bot no Telegram deve interagir com os usuários e responder de acordo com os dados
# do sistema.
# ● Persistência dos Dados para armazenar e recuperar informações (CSV, JSON ou
# outro).
# ● Código organizado e bem estruturado
# ● Apresentação do sistema, demonstrando as funcionalidades implementadas

# Critérios de Avaliação (200 pontos):
# Funcionalidade e requisitos atendidos (50 pontos): O sistema funciona corretamente e
# implementa os requisitos básicos?
# Qualidade do código (50 pontos): O código está bem organizado, com boas práticas e uso
# eficiente de recursos?
# Integração entre terminal e bot (50 pontos): A comunicação entre as áreas do gestor e
# atendimento via bot está fluida e eficiente?
# Apresentação (50 pontos): O grupo conseguiu explicar o funcionamento do sistema e
# demonstrar as principais funcionalidades?

# Entrega:
# Data limite: Até o último dia do módulo
# Formato: Enviar um arquivo .zip ou link para repositório no GitHub.

# Grupos de no máximo 3 participante

import smtplib
import json
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler,filters, MessageHandler
import random


global r
global menu
global relatorio
global lista_pedidos
global username
global nome
global sobrenome
global nome_comp
global cliente_email
global hora
global data
global datahora
global cliente
global lista_email_cliente

hora = datetime.now().strftime('%H:%M:%S')
data = datetime.now().strftime('%d-%m-%Y')
datahora = data + " " + hora

# with open('Trabalho Final Desenvolvimento de um Sistema Integrado com Bot no Telegram\\menu.json', 'w') as arquivo:
#     arquivo = open('Trabalho Final Desenvolvimento de um Sistema Integrado com Bot no Telegram\\menu.json', 'w')

# with open('Trabalho Final Desenvolvimento de um Sistema Integrado com Bot no Telegram\\relatorio de vendas.json', 'w') as arquivo:
#     arquivo = open('Trabalho Final Desenvolvimento de um Sistema Integrado com Bot no Telegram\\relatorio de vendas.json', 'w')

relatorio = open('Trabalho Final Desenvolvimento de um Sistema Integrado com Bot no Telegram\\relatorio de vendas.json', 'r', encoding="utf-8")

r = 's'

# menu = {"Cheesenoffee": "R$:24,90", "Holanoffee": "R$:24,90", "Maranutella": "R$:25,90", "Coca-cola 500 ml": "R$:6,00","Fanta Laranja 500 ml": "R$:5,00","Guarana 600 ml": "R$:6,00"}

# with open('Trabalho Final Desenvolvimento de um Sistema Integrado com Bot no Telegram\\menu.json', 'w', encoding="utf-8") as arquivo:
#     json.dump(menu,arquivo)

arquivo_menu = open('Trabalho Final Desenvolvimento de um Sistema Integrado com Bot no Telegram\\menu.json', 'r', encoding="utf-8")
menu = json.load(arquivo_menu)

def resposta():
    global r
    print("s para continuar a operar o menu")
    r = input("Deseja realizar outra operação no menu?: ")


def enviar_email_relatorio_de_vendas():
    from email.message import EmailMessage
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login('guilhermeyu@gmail.com', 'tbjt ktbf utoy lpgt')
    msg = EmailMessage()
    msg['To'] = 'ueda.guilherme@yahoo.com.br'
    msg['Subject'] = 'Revisão Positiva'
    msg['From'] = 'guilhermeyu@gmail.com'
    with open('Bot de Atendimento ao Cliente\\reposta positiva.txt', 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    msg.set_content(conteudo)
    servidor.send_message(msg)
    servidor.quit()
    print("E-mail enviado")

def enviar_email_promoções():
    from email.message import EmailMessage
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login('guilhermeyu@gmail.com', 'tbjt ktbf utoy lpgt')
    msg = EmailMessage()
    for cliente in lista_email_cliente:
        msg['To'] = cliente
        msg['Subject'] = 'Revisão Positiva'
        msg['From'] = 'guilhermeyu@gmail.com'
        with open('Bot de Atendimento ao Cliente\\reposta positiva.txt', 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        msg.set_content(conteudo)
        servidor.send_message(msg)
    servidor.quit()
    print("E-mail enviado")

def area_do_gestor():
    global r
    global menu
    print("============================ OPERAÇÕES DO MENU ============================")
    print("1 - Adicionar item ao menu")
    print("2 - Remover item do menu")
    print("3 - Modificar preço de um item no menu")    
    print("============================ OPERAÇÕES DO MENU ============================")
    operação = int(input("Informe o numero da operação que deseja realizar: "))
    if operação == 1:
        print("============================ ADICIONAR ============================")
        nome = input("Informe o nome do novo item: ")
        preço = float(input("Informe o preço do novo produto: "))
        preço_formatado = "R$:" + str(preço)
        menu[nome] = preço_formatado
        print(f'O produto: {nome} que possui o preço: {preço_formatado} foi adicionado com sucesso')
        with open('Trabalho Final Desenvolvimento de um Sistema Integrado com Bot no Telegram\\menu.json', 'w', encoding="utf-8") as arquivo:
            json.dump(menu,arquivo)
        resposta()
    elif operação == 2:
        print("============================ REMOVER ============================")
        remover = input("Informe o produto que deseja remover: ")
        for item in menu:
            if menu[item] == remover:
                valor_a_remover = menu.pop(remover)
                print(f'Item removido {valor_a_remover}')
        print(f'O produto {item} foi removido')
        print(menu)
        resposta()
    elif operação == 3:
        print("============================ MODIFICAR PREÇO ============================")
        modificar = input("Informe o produto que deseja modificar o preço: ")
        novo_preço = int(input("Informe o novo preço do produto: "))
        for item in menu:
            if modificar == item["nome"]:
                menu["nome" == modificar]["preço"] = novo_preço
                print(f'O preço do produto: {item} foi atualizada')
            else:
                print("Falso")
        resposta()


while r =='s':
    area_do_gestor()