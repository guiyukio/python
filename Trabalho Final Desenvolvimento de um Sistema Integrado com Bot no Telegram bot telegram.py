import smtplib
import json
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler
from telegram.ext import filters, MessageHandler

global r
global menu
global relatorios
global lista_pedidos
global username
global bot
global nome
global sobrenome
global nome_comp
global cliente_email
global hora
global data
global datahora
global datahora_string
global cliente
global lista_email_cliente
global id_pedido
global valor_total
global positivas
global negativas
global contador_positivas
global contador_negativas
global data_previsão
global hora_previsão


logs_negativas = open('Trabalho Final Desenvolvimento de um Sistema '
'Integrado com Bot no Telegram\\logs negativas.json', 'r')
logs_positivas = open('Trabalho Final Desenvolvimento de um Sistema '
'Integrado com Bot no Telegram\\logs positivas.json', 'r')

arquivo_menu = open('Trabalho Final Desenvolvimento de um Sistema '
'Integrado com Bot no Telegram\\menu.json', 'r', encoding="utf-8")
menu = json.load(arquivo_menu)

arquivo_relatorio = open('Trabalho Final Desenvolvimento de um Sistema '
'Integrado com Bot no Telegram\\relatorio de vendas.json', 'r', encoding="utf-8")
relatorios = json.load(arquivo_relatorio)

arquivo_pedido = open("Trabalho Final Desenvolvimento de um Sistema "
"Integrado com Bot no Telegram\\pedidos.json", 'r', encoding="utf-8")
pedidos = json.load(arquivo_pedido)

hora = datetime.now().strftime('%H:%M:%S')
data = datetime.now().strftime('%d-%m-%Y')
datahora = data + " " + hora
datahora_string = str(datahora)

positivas = ["excelente","otima","bom","satisfatorio","maravilhoso","fantastico","impressionante",
             "excepcional","magnifico","completo","inovador","avançado","moderno","premium"]
negativas = ["ruim","pessimo","insatisfatorio","fraco","decepcionante","terrivel","horrivel",
             "lamentavel","inaceitavel","medíocre","instabilidades","insatisfatórios","inadequada"]

contador_positivas = 0
contador_negativas = 0

def enviar_email_confirmando_pedidos(nome_comp):
    global hora
    global data
    global lista_pedidos
    global cliente_email
    global datahora_string
    global nome_completo_string
    global relatorio
    global valor_total
    global nome_completo_string
    global pedidos
    global hora_previsão
    global data_previsão
    nome_completo_string = str(nome_comp)
    for pedido in pedidos:
        if pedido.startswith(nome_completo_string):
            pedido_atual = pedido
            status_atual = pedidos[pedido_atual]
    hora_separada = hora.split(":")
    hora_int = int(hora_separada[0])
    hora_int = hora_int + 1
    if hora_int >=24:
        data_separada = data.split("-")
        dia_int = int(data_separada[0])
        dia_int = dia_int + 1
        dia_int_str = str(dia_int)
        data_previsão = dia_int_str + "-" + hora_separada[1] + "-" + hora_separada[2]
        print(data_previsão)
        return data_previsão
    else: 
        data_previsão = data
    hora_int_str = str(hora_int + 1)
    hora_previsão = hora_int_str + ":" + hora_separada[1] + ":" + hora_separada[2]
    print(hora_previsão)
    from email.message import EmailMessage
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login('EMAIL A SER LOGADO', 'CODIGO DE SEGURANÇA DO EMAIL')
    msg = EmailMessage()
    msg['To'] = cliente_email
    msg['Subject'] = 'Confirmação de Pedido - Trabalho final'
    msg['From'] = 'REMETENTE DO EMAIL'
    msg.add_alternative(f"""
        <html>
         <body>
         <h1>Prezado(a) {nome_completo_string},</h1>
         <p1>Agradecemos por escolher o nosso estabelecimento! Temos o prazer de confirmar o seu pedido.</p1><br>
         <p2></p2><br>
         <p3>Número do Pedido: {pedido_atual}</p3><br>
         <p4></p4><br>
         <p5>  ● Pedido Aceito as: </p5><br>
         <p6>    {data} : {hora} : {status_atual} </p6><br>
         <p7></p7><br>
         <p8>  ● Previsão de Entrega as:</p8><br>
         <p9>    {data_previsão} : {hora_previsão} </p9><br>
         <p10>    total : {valor_total} </p10><br>
         <p11></p11><br>
         <p12>Agradecemos pela sua preferência e esperamos que desfrute da sua refeição!</p12><br>
         <p13></p13><br>
         <p14>Atenciosamente,</p14><br>
         <p15></p15><br>
         <p16>UEDA'S BOT</p16><br>
         </body>
        </html>
        """, subtype='html')
    servidor.send_message(msg)
    servidor.quit()
    print("E-mail enviado")

def pre_processamento(pedido):
    global lista_plavras
    pedido_minuscula = pedido.lower()
    pedido_minuscula_sem_virgula = pedido_minuscula.replace(",","")
    pedido_sem_pontuação = pedido_minuscula_sem_virgula.replace(".","")
    lista_plavras = pedido_sem_pontuação.split(" ")

def classificação():
    global contador_positivas
    global contador_negativas
    global lista_plavras
    for palavra in lista_plavras:
        if palavra in positivas:
            contador_positivas += 1
    for palavra in lista_plavras:
        if palavra in negativas:
            contador_negativas += 1

def salvando_logs_positivas(nome_comp):
    global logs_positivas
    id = 1
    string_nome_completo = str(nome_comp)
    log_string_nome_completo = string_nome_completo + " " + str(id)
    arquivo_logs = open('Trabalho Final Desenvolvimento de um Sistema '
    'Integrado com Bot no Telegram\\logs positivas.json', 'r', encoding="utf-8")
    logs = json.load(arquivo_logs)
    for log in logs:
        if log == log_string_nome_completo:
            log_separada = log_string_nome_completo.split(" ")
            idlog = int(log_separada[2])
            idlog = idlog + 1
            log_string_nome_completo = log_separada[0] + " " + log_separada[1] + " " + str(idlog)
    logs[log_string_nome_completo] = datahora
    with open('Trabalho Final Desenvolvimento de um Sistema '
    'Integrado com Bot no Telegram\\logs positivas.json', 'w') as arquivo:
        json.dump(logs,arquivo)
    print("Log Positiva salva com sucesso")

def salvando_logs_negativas(nome_comp):
    global logs_negativas
    global datahora_string
    string_nome_completo = str(nome_comp)
    id = 1
    log_string_cliente_email = string_nome_completo + " " + str(id)
    arquivo_logs = open('Trabalho Final Desenvolvimento de um Sistema '
    'Integrado com Bot no Telegram\\logs negativas.json', 'r', encoding="utf-8")
    logs = json.load(arquivo_logs)
    for log in logs:
        if log == log_string_cliente_email:
            log_separada = log_string_cliente_email.split(" ")
            idlog = int(log_separada[1])
            idlog = idlog + 1
            log_string_cliente_email = log_separada[0] + " " + str(idlog)
    logs[log_string_cliente_email] = datahora
    with open('Trabalho Final Desenvolvimento de um Sistema '
    'Integrado com Bot no Telegram\\logs negativas.json', 'w') as arquivo:
        json.dump(logs,arquivo)
    print("Log Negativa salva com sucesso")

def enviar_email_revisão_positivo(nome_comp):
    string_nome_completo = str(nome_comp)
    from email.message import EmailMessage
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login('EMAIL A SER LOGADO', 'CODIGO DE SEGURANÇA DO EMAIL')
    msg = EmailMessage()
    msg['To'] = 'DESTINATARIO DO EMAIL'
    msg['Subject'] = f'Revisão Positiva de {string_nome_completo}'
    msg['From'] = 'REMETENTE DO EMAIL'
    with open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\revisão.txt", 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    msg.set_content(f'{conteudo}')
    servidor.send_message(msg)
    servidor.quit()
    print("E-mail enviado")

def enviar_email_revisão_negativa(nome_comp):
    string_nome_completo = str(nome_comp)
    from email.message import EmailMessage
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login('EMAIL A SER LOGADO', 'CODIGO DE SEGURANÇA DO EMAIL')
    msg = EmailMessage()
    msg['To'] = 'DESTINATARIO DO EMAIL'
    msg['Subject'] = f'Revisão Negativa de {string_nome_completo}'
    msg['From'] = 'REMETENTE DO EMAIL'
    with open('Trabalho Final Desenvolvimento de um Sistema '
    'Integrado com Bot no Telegram\\revisão.txt', 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    msg.set_content(f'{conteudo}')
    msg.set_content(conteudo)
    servidor.send_message(msg)
    servidor.quit()
    print("E-mail enviado")

def salvar_no_relatorio_e_salvar_pedido():
    global lista_pedidos
    global cliente_email
    global datahora_string
    global nome_completo_string
    global relatorio
    global valor_total
    id = 1
    id_relatorio = datahora + ' ' + nome_completo_string + ' ' + str(id)
    id_pedido = nome_completo_string + ' ' + str(id)
    for relatorio in relatorios:
        if relatorio == id_relatorio:
            id_relatorio_separado = id_relatorio.split(" ")
            idlog = int(id_relatorio_separado[4])
            idlog = idlog + 1
            id_pedido = id_relatorio_separado[0] + " " + id_relatorio_separado[1] + " " + id_relatorio_separado[2] + " " +id_relatorio_separado[3] + " " + str(idlog)
    for pedido in pedidos:
        if pedido == id_pedido:
            id_pedido_separado = id_pedido.split(" ")
            idlog = int(id_pedido_separado[2])
            idlog = idlog + 1
            id_pedido =  id_pedido_separado[0] + " " + id_pedido_separado[1] + " " + str(idlog)
    relatorios[id_relatorio] = valor_total
    pedidos[id_pedido] = "Em preparo"

    with open('Trabalho Final Desenvolvimento de um Sistema '
    'Integrado com Bot no Telegram\\relatorio de vendas.json', 'w') as arquivo:
        json.dump(relatorios,arquivo)
    
    with open('Trabalho Final Desenvolvimento de um Sistema '
    'Integrado com Bot no Telegram\\pedidos.json', 'w') as arquivo:
        json.dump(pedidos,arquivo)

async def start(update : Update, context) -> None:
    global nome
    global sobrenome
    global nome_comp
    global nome_completo_string
    nome = update.effective_user.first_name
    sobrenome = update.effective_user.last_name
    nome_comp = nome + " " + sobrenome
    nome_completo_string = str(nome_comp)
    await update.message.reply_text(f"Olá {nome_comp}")
    await update.message.reply_text("Eu Sou um Bot simples Criado como teste.")
    await update.message.reply_text("para fazer seu pedido /pedido.")
    await update.message.reply_text("Para ver o cardapio /cardapio")
    await update.message.reply_text("Para ter ajuda: /ajuda")
    await update.message.reply_text("Para ver a lista de comandos: /help ")
    await update.message.reply_text("Para ver a imagem do item: /imagemCheesenoffee "
    "/imagemHolanoffee /imagemMaranutell ")
    await update.message.reply_text("Para ver a imagem do item: /imagemGuarana "
    "/imagemCoca /imagemFantaLaranja ")
    await update.message.reply_text("Informe seu e-mail: ")
    await update.message.reply_text("Sera considerado um email qualquer input com: @ ")

async def help(update : Update, context) -> None:
    await update.message.reply_text("para fazer seu pedido /pedido.")
    await update.message.reply_text("Para ver o cardapio /cardapio")
    await update.message.reply_text("Para ter ajuda de como pedir: /ajuda")
    await update.message.reply_text("Para ver a imagem do item: /imagemCheesenoffee "
    "/imagemHolanoffee /imagemMaranutell ")
    await update.message.reply_text("Para ver a imagem do item: /imagemGuarana "
    "/imagemCoca /imagemFantaLaranja ")
    await update.message.reply_text("para acompanhar o pedido: /Acompanhar_o_pedido.")
    await update.message.reply_text("para avaliar o atendimento: /Avaliar_Atendimento.")


async def cardapio(update : Update, context) -> None:
    global menu
    id = 1
    for item in menu:
        valor = menu[item]
        await update.message.reply_text(f"{id} - {item} : {valor}")
        id = id + 1
    await update.message.reply_text("Para ver a imagem do item: /imagemCheesenoffee "
    "/imagemHolanoffee /imagemMaranutell ")
    await update.message.reply_text("Para ver a imagem do item: /imagemGuarana "
    "/imagemCoca /imagemFantaLaranja ")

async def ajuda(update : Update, context) -> None:
    await update.message.reply_text("O pedido sera separado por virgula(,)")
    await update.message.reply_text("Exemplo de como o pedido deve ser feito:")
    await update.message.reply_text("2 Holanoffee, 4 Marunutella, 3 Guarana, 3 Coca-cola")

async def imagemCheesenoffee(update : Update, context) -> None:
    imagemCheesenoffee = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\cheessenoffee.png", "rb")
    await update.message.reply_text("Cheesenoffee: ")
    await update.message.reply_photo(imagemCheesenoffee)

async def imagemHolanoffee(update : Update, context) -> None:
    imagemHolanoffee = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\holanoffee.png", "rb")
    await update.message.reply_text("Holanoffee: ")
    await update.message.reply_photo(imagemHolanoffee)

async def imagemMaranutella(update : Update, context) -> None:
    imagemMaranutella = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\maranutella.png", "rb")
    await update.message.reply_text("Maranutella: ")
    await update.message.reply_photo(imagemMaranutella)

async def imagemGuarana(update : Update, context) -> None:
    imagemGuarana = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\guarana.png", "rb")
    await update.message.reply_text("Guarana: ")
    await update.message.reply_photo(imagemGuarana)

async def imagemCoca(update : Update, context) -> None:
    imagemCoca = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\coca.png", "rb")
    await update.message.reply_text("Coca-Cola: ")
    await update.message.reply_photo(imagemCoca)

async def imagemFantaLaranja(update : Update, context) -> None:
    imagemFantaLaranja = open("Trabalho Final Desenvolvimento de um Sistema "
    "Integrado com Bot no Telegram\\fanta-laranja.png", "rb")
    await update.message.reply_text("Fanta Laranja: ")
    await update.message.reply_photo(imagemFantaLaranja)
    
async def Acompanhar_o_pedido(update : Update, context) -> None:
    global nome
    global sobrenome
    global nome_comp
    global nome_completo_string
    global pedidos
    nome = update.effective_user.first_name
    sobrenome = update.effective_user.last_name
    nome_comp = nome + " " + sobrenome
    nome_completo_string = str(nome_comp)
    for pedido in pedidos:
        if pedido.startswith(nome_completo_string):
            pedido_atual = pedido
            status_atual = pedidos[pedido_atual]
    await update.message.reply_text(f"{pedido_atual} : {status_atual}")

async def Avaliar_Atendimento(update : Update, context) -> None:
    await update.message.reply_text(f"Deseja realizar um avaliação do atendimento? ")
    await update.message.reply_text(f"Para realizar a avaliação escreva: ")
    await update.message.reply_text(f"Avaliação/")

async def pedido(update : Update, context) -> None:
    global lista_pedidos
    global cliente_email
    global nome
    global sobrenome
    global nome_comp
    global datahora
    global valor_total
    global nome_completo_string
    valor_total = 0
    nome = update.effective_user.first_name
    sobrenome = update.effective_user.last_name
    nome_comp = nome + " " + sobrenome
    nome_completo_string = str(nome_comp)
    pedido = update.message.text
    if pedido.endswith(".com") or pedido.endswith(".br"):
        cliente_email = update.message.text
        await update.message.reply_text("E-mail guardado.")
    elif pedido.startswith("Avaliação/"):
        with open("Trabalho Final Desenvolvimento de um Sistema "
        "Integrado com Bot no Telegram\\revisão.txt", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(pedido)
        pre_processamento(pedido)
        classificação()
        if contador_positivas > contador_negativas:
            await update.message.reply_text("Agradecemos pela sua revisão, "
            "e ficamos feliz com a sua experiencia Positiva")      
            enviar_email_revisão_positivo(nome_comp)
            salvando_logs_positivas(nome_comp)
        elif contador_negativas > contador_positivas:
            await update.message.reply_text("Agradecemos pela sua revisão, e "
            "pedimos desculpas pela sua experiencia Negativa")
            enviar_email_revisão_negativa(nome_comp)
            salvando_logs_negativas(nome_comp,datahora_string)
    else:
        lista_pedido = pedido.split(",")
        for item in lista_pedido:
            valores_de_item = item.split(" ")
            valores_filtrados = list(filter(None,valores_de_item))
            for valor in valores_filtrados:
                if valor.isdigit():
                    quantidade = int(valor)
                else:
                    for opção in menu:
                        if opção == valor:
                            valor_com_cifrão = menu[opção]
                            valor_numeros = valor_com_cifrão.strip("R$:")
                            valor = valor_numeros.replace(",",".")
                            valor = float(valor)
                            valor_por_item = (valor * quantidade)
                            valor_total = valor_total + valor_por_item
        await update.message.reply_text(f"O valor total do pedido é: {valor_total} ")
        salvar_no_relatorio_e_salvar_pedido()
        enviar_email_confirmando_pedidos(nome_comp)
    await update.message.reply_text("Para ver a lista de comandos: /help ")

def main():
    token = "CODIGO DO BOT"
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cardapio", cardapio))
    application.add_handler(CommandHandler("ajuda", ajuda))
    application.add_handler(CommandHandler("imagemCheesenoffee", imagemCheesenoffee))
    application.add_handler(CommandHandler("imagemHolanoffee", imagemHolanoffee))
    application.add_handler(CommandHandler("imagemMaranutella", imagemMaranutella))
    application.add_handler(CommandHandler("imagemGuarana", imagemGuarana))
    application.add_handler(CommandHandler("imagemCoca", imagemCoca))
    application.add_handler(CommandHandler("imagemFantaLaranja", imagemFantaLaranja))
    application.add_handler(CommandHandler("Acompanhar_o_pedido", Acompanhar_o_pedido))
    application.add_handler(CommandHandler("Avaliar_Atendimento", Avaliar_Atendimento))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(MessageHandler(filters.TEXT, pedido))
    print("Bot está rodando...")
    application.run_polling()


main()