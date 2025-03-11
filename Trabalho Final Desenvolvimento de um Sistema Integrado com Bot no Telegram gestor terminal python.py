import smtplib
import json
from datetime import datetime


global r
global menu
global relatorio
global lista_pedidos
global cliente_email
global hora
global data
global datahora
global cliente
global lista_email_cliente
global pedidos

hora = datetime.now().strftime('%H:%M:%S')
data = datetime.now().strftime('%d-%m-%Y')
datahora = data + " " + hora

r = 's'

arquivo_menu = open('Trabalho Final Desenvolvimento de um Sistema '
'Integrado com Bot no Telegram\\menu.json', 'r', encoding="utf-8")
menu = json.load(arquivo_menu)

arquivo_relatorio = open('Trabalho Final Desenvolvimento de um Sistema '
'Integrado com Bot no Telegram\\relatorio de vendas.json', 'r', encoding="utf-8")
relatorios = json.load(arquivo_relatorio)

arquivo_pedido = open("Trabalho Final Desenvolvimento de um Sistema "
"Integrado com Bot no Telegram\\pedidos.json", "r", encoding="utf-8")
pedidos = json.load(arquivo_pedido)

def resposta():
    global r
    print("s para continuar a operar o menu")
    r = input("Deseja realizar outra operação no menu?: ")


def enviar_email_relatorio_de_vendas():
    global relatorios
    arquivo = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\json to txt.txt", "w")
    json.dump(relatorios, arquivo)
    from email.message import EmailMessage
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login('EMAIL A SER LOGADO', 'CODIGO DE SEGURANÇA DO EMAIL')
    msg = EmailMessage()
    msg['To'] = 'DESTINATARIO DO EMAIL'
    msg['Subject'] = 'Relatorio de Vendas'
    msg['From'] = 'REMETENTE DO EMAIL'
    arquivo = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\json to txt.txt", "r", encoding="utf-8")
    conteudo = arquivo.read()
    msg.add_attachment(conteudo, 
    subtype='txt', 
    filename='Relatorios.txt')
    servidor.send_message(msg)
    servidor.quit()
    arquivo.close()
    print("E-mail enviado")

def enviar_email_relatorio_de_vendas_diarias():
    global relatorios
    relatorio_diario = []
    for relatorio in relatorios:
        if relatorio.startswith(data):
            relatorio_diario = relatorio
            arquivo = open("Trabalho Final Desenvolvimento de um Sistema "
            "Integrado com Bot no Telegram\\relatorio diario.txt", "w")
    json.dump(relatorio_diario, arquivo)
    from email.message import EmailMessage
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login('EMAIL A SER LOGADO', 'CODIGO DE SEGURANÇA DO EMAIL')
    msg = EmailMessage()
    msg['To'] = 'DESTINATARIO DO EMAIL'
    msg['Subject'] = 'Relatorio de Vendas Diarias'
    msg['From'] = 'REMETENTE DO EMAIL'
    arquivo = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\relatorio diario.txt", "r", encoding="utf-8")
    conteudo = arquivo.read()
    msg.add_attachment(conteudo, 
    subtype='txt', 
    filename='relatorio diario.txt')
    servidor.send_message(msg)
    servidor.quit()
    arquivo.close()
    print("E-mail enviado")

def enviar_email_promoções():
    from email.message import EmailMessage
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login('EMAIL A SER LOGADO', 'CODIGO DE SEGURANÇA DO EMAIL')
    msg = EmailMessage()
    for cliente in lista_email_cliente:
        msg['To'] = cliente
        msg['Subject'] = 'Revisão Positiva'
        msg['From'] = 'REMETENTE DO EMAIL'
        with open('Bot de Atendimento ao Cliente\\reposta positiva.txt', 
                  'r', encoding="utf-8") as arquivo:
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
    print("4 - Gerenciar status de pedido")      
    print("5 - Enviar o Relatorio de vendas para o E-MAIL") 
    print("6 - Enviar o Relatorio de vendas diarias para o E-MAIL")     
    print("============================ OPERAÇÕES DO MENU ============================")
    operação = int(input("Informe o numero da operação que deseja realizar: "))
    if operação == 1:
        print("============================ ADICIONAR ============================")
        nome = input("Informe o nome do novo item: ")
        preço = float(input("Informe o preço do novo produto: "))
        preço_formatado = "R$:" + str(preço)
        menu[nome] = preço_formatado
        print(f'O produto: {nome} que possui o preço: {preço_formatado} foi adicionado com sucesso')
        with open('Trabalho Final Desenvolvimento de um Sistema '
        'Integrado com Bot no Telegram\\menu.json', 'w', encoding="utf-8") as arquivo:
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
    elif operação == 4:
        global pedidos
        print("============================ Gerenciar Status ============================")
        modificar = input("Informe o pedido que deseja modificar o status: ")
        print("Informe o numero do valor do status para modificar o valor: ")
        print("1 - Em Preparo")
        print("2 - Pronto")
        print("3 - Entregue")
        novo_valor_do_status = int(input("Informe o novo status do produto: "))
        if novo_valor_do_status == 1:
            novo_valor_do_status = 'Em Preparo'
        elif novo_valor_do_status == 2:
            novo_valor_do_status = 'Pronto'
        elif novo_valor_do_status == 3:
            novo_valor_do_status = 'Entregue'

        for pedido in pedidos:
            if modificar == pedido:
                pedidos[modificar] = novo_valor_do_status
                print(f"Valor mudado para {novo_valor_do_status}")
            else:
                print("Falha na Mudança de Status")
            
        with open('Trabalho Final Desenvolvimento de um Sistema '
        'Integrado com Bot no Telegram\\pedidos.json', 'w') as arquivo:
            json.dump(pedidos,arquivo)
        resposta()
    elif operação == 5:
        print("============================ ENVIANDO RELATORIO ============================")
        enviar_email_relatorio_de_vendas()
        resposta()
    elif operação == 6:
        print("============================ ENVIANDO RELATORIO DIARIO ============================")
        enviar_email_relatorio_de_vendas_diarias()
        resposta()


while r =='s':
    area_do_gestor()