import datetime

def abrir_arquivo():
    arquivo = open('PERIODOS/03-03---04--09.txt',encoding='utf-8') 
    return arquivo

def fechar_arquivo(arquivo):
    arquivo.close()
    return

def extrai_dados(arquivo):
    #retorna lista iniciando por nome do exame e depois listas de cts
    lista = arquivo.readlines() 
    return lista

def regioes(opcao, listaCTS):

    tabela = ['AM','RR','AP','PA','TO','RO','AC', #0 = NORTE
              'MA','PI','CE','RN','PE','PB','SE','AL','BA', #1 = NORDESTE
              'MT','MS','GO','DF', #2 = CENTROOESTE
              'RJ','SP','ES','MG', #3 = SUDESTE
              'PR','RS','SC'] #4 = SUL
               


    reg_norte = list() 
    reg_nordeste = list() 
    reg_centroOeste = list() 
    reg_sudeste = list() 
    reg_sul = list() 

    for i in range(len(listaCTS)):

        vec_aux_padrao = listaCTS[i]
        vec_aux_splitado = listaCTS[i].split('\n')

        if vec_aux_splitado[0][-2:] in tabela:
            if 6 >= tabela.index(vec_aux_splitado[0][-2:]) >= 0:
                reg_norte.append(vec_aux_padrao)
            elif 15 >= tabela.index(vec_aux_splitado[0][-2:]) > 6:
                reg_nordeste.append(vec_aux_padrao)
            elif 19 >= tabela.index(vec_aux_splitado[0][-2:]) > 15:
                reg_centroOeste.append(vec_aux_padrao)
            elif 23 >= tabela.index(vec_aux_splitado[0][-2:]) > 19:
                reg_sudeste.append(vec_aux_padrao)
            elif 26 >= tabela.index(vec_aux_splitado[0][-2:]) > 23:
                reg_sul.append(vec_aux_padrao)

    if opcao == 1:
        return reg_norte
    if opcao == 2:
        return reg_nordeste
    if opcao == 3:
        return reg_centroOeste
    if opcao == 4:
        return reg_sudeste
    if opcao == 5:
        return reg_sul
    return

def menu():
    print("ESCOLHA O QUE DESEJA SABER:")
    print("1 - TIPO DE EXAME")
    print("2 - NOMES DOS CENTROS DE TESTES EM QUESTÃO")
    print("3 - CENTROS DE TESTES COM VAGAS EM 30 DIAS")
    print("4 - VAGAS EM JULHO")
    print("5 - PESQUISA POR REGIÃO")
    opcao = int(input())
    return opcao

def operacao(opcao, arquivo, exameDeCert):
    #TIPO DE EXAME
    if opcao == 1:
        print(exameDeCert)

    #NOMES DOS CTS
    elif opcao == 2:
        listar_cts(arquivo)

    #VAGAS EM ATÉ 30 DIAS
    elif opcao == 3:

        cts_formatados = list()
        for i in range(len(arquivo)):
            cts_formatados.append(transforma_datas(arquivo[i]))

        cts_sem_formatar = list()
        for i in range(len(arquivo)):
            cts_sem_formatar.append(arquivo[i].split('\n'))

        for i in range(len(cts_formatados)):
            cont = 0
            qtd_vagas_ct = 0
            for j in range(1, len(cts_formatados[i])):
                if (cts_formatados[i][j] - datetime.datetime.today()).days < 30 and (cts_formatados[i][j] - datetime.datetime.today()).days > 0:
                    qtd_vagas_ct += int(cts_sem_formatar[i][j][40])
                    cont += 1
                    if cont == 1:
                        print("O {} possui vagas para os proximos 30 dias".format(cts_formatados[i][0]))
                    print("{}".format(cts_sem_formatar[i][j]))
            if cont == 0:
                print("O {} NÃO possui vagas para os proximos 30 dias".format(cts_formatados[i][0]))
            print("Total de {} vagas para os proximos 30 dias\n".format(qtd_vagas_ct))

    #VAGAS P/ JUNHO
    elif opcao == 4:

        cts_formatados = list()
        for i in range(len(arquivo)):
            cts_formatados.append(transforma_datas(arquivo[i]))

        #Datas formatadas para cálculo

        cts_sem_formatar = list()
        for i in range(len(arquivo)):
            cts_sem_formatar.append(arquivo[i].split('\n'))

        #Datas formatadas para exibição

        for i in range(len(cts_formatados)):
            cont = 0
            qtd_vagas_ct = 0
            for j in range(1, len(cts_formatados[i])):
                if (cts_formatados[i][j] - datetime.datetime.today()).days < 30 and (cts_formatados[i][j] - datetime.datetime.today()).days > 0:
                    qtd_vagas_ct += int(cts_sem_formatar[i][j][40])
                    cont += 1
                    if cont == 1:
                        print("O {} possui vagas para os proximos 30 dias".format(cts_formatados[i][0]))
                    print("{}".format(cts_sem_formatar[i][j]))

    elif opcao == 5:
        reg = int(input("Qual região você deseja saber a respeito?\n1 - NORTE\n2 - NORDESTE\n3 - CENTRO OESTE\n4 - SUDESTE\n5 - SUL\n"))
        cts_da_regiao = regioes(reg, arquivo)
        for i in range(len(cts_da_regiao)):
            para_print = cts_da_regiao[i].split('\n')
            print(str(i+1) + ' - ' + para_print[0][4:])

    return

def transforma_datas(centro_de_testes):
    lista = centro_de_testes.split('\n')
    retorno = list()
    retorno.append(lista[0])

    for i in range(1, len(lista)):
        retorno.append(datetime.datetime.strptime(lista[i][6:16] + ' ' + lista[i][25:30], '%d/%m/%Y %H:%M'))
    return retorno

def listar_cts(listaDeArquivo):
    cts = list()
    cont = 1
    for i in range(len(listaDeArquivo)):
        cts.append(listaDeArquivo[i].split('\n'))
    for i in cts:
        print('{} - {}'.format(cont,i[0].replace('CT: ','')))
        cont += 1
    return

def exibir_datas(ct):
    lista = ct.split('\n')
    for i in range(1,len(lista)):
        print(lista[i])
    return



#### MAIN ####

arquivo = abrir_arquivo() 
dados = extrai_dados(arquivo)
fechar_arquivo(arquivo) 

tipo_de_exame = (dados.pop(0))[7:]

'''op = 1 
while op == 1: 
    operacao(menu(), listaArquivo, exame)
    op = int(input("\nDeseja realizar outra pesquisa? 1 - SIM / 2 - NÃO: ")) #PILHA
    print('')
print('Programa finalizado com sucesso!')'''

'''for i in range(len(dados)):
    print(dados[i])'''

#print(dados)

dados_totais    = []
nomes_cts       = []
vagas_cts       = []
dia_vagas       = []

print(dados)

for i in range(len(dados)):
    nome_ct     = ''
    dia_vagas   = []
    vagas_cts   = []
    if dados[i][:3] == "CT:":
        nomes_sem_barraN = dados[i].replace("\n", "")
        nomes_ct = nomes_sem_barraN.replace("CT: ", "")
    elif dados[i] == '\n':
        nomes_cts.append(nome_ct)
        vagas_cts.append()
        dia_vagas.append()
        
for j in nomes_cts:
    print(j)
    
