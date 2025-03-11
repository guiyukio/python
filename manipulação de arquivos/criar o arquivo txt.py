with open('alunos.txt', 'w') as arquivo:
    arquivo = open('alunos.txt','w')

with open('alunos.txt','a') as arquivo:
    arquivo.writelines(["'nome': 'Guilherme'\n",
                        "'matrícula': '1242516' \n", 
                        "'idade': '25' \n", 
                        "'curso': 'ADS' \n",
                        "''\n",
                        "'nome': 'Fulano'\n",
                        "'matrícula': '1256721'\n",
                        "'idade': '27'\n",
                        "'curso': 'ADS'\n"])
    