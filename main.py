def abrir_arquivo():
	arquivo = open('dados/05-23---07-23.txt', encoding='utf-8')
	return arquivo


def fechar_arquivo(arquivo):
	arquivo.close()
	return


def extrai_dados(arquivo):
	#retorna lista iniciando por nome do exame e depois listas de cts
	lista = arquivo.readlines()
	return lista


def formata_dados(arquivo):
	#função recebe um arquivo em lista e retorna seus valores em variaveis

	#variaveis de retorno principal
	nomes_cts = []
	dia_hora_vagas = []

	#variáveis auxiliares
	ct = []

	for i in range(len(arquivo)):

		if arquivo[i][:3] == "CT:":
			#formato o nome do ct para a variavel nome_ct
			nomes_sem_barraN = arquivo[i].replace("\n", "")
			nome_ct = nomes_sem_barraN.replace("CT: ", "")
			nomes_cts.append(nome_ct)
			dia_hora_vagas.append(ct)
			ct = []
		elif arquivo[i][:4] == "Data":
			if len(arquivo[i]) == 42:
				ct.append(
				    (arquivo[i][6:16], arquivo[i][25:30], arquivo[i][-2]))
			elif len(arquivo[i]) == 43:
				ct.append(
				    (arquivo[i][6:16], arquivo[i][25:30], arquivo[i][-3:-1]))
			elif len(arquivo[i]) == 44:
				ct.append(
				    (arquivo[i][6:16], arquivo[i][25:30], arquivo[i][-4:-1]))
           
	dia_hora_vagas.append(ct)

	return nomes_cts, dia_hora_vagas[1:]


def verificaBarraN(texto):
	if texto == "\n":
		return False
	else:
		return True


def vagasTotaisPorMes(mes, dados):
	vagas = 0

	for i in dados:
		for x in i:
			if x[0][3:5] == mes:
				vagas += int(x[2])

	return vagas


def vagasPorUF(nome_cts, dados):
    UFs = ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"]

    mes = int(input("Digite o mês desejado: "))

    total = 0

    for i in range(len(UFs)):
        vagas = 0
        for j in range(len(nome_cts)):
            if nome_cts[j][-2:] == UFs[i]:
                for k in range(len(dados[j])):
                    if int(dados[j][k][0][3:5]) == mes: #Soma apenas o mes solicitado
                        vagas += int(dados[j][k][2])
        print("{}: {}".format(UFs[i],vagas))
        total += vagas

    print("\nTotal:",total)
    return 


def vagasPorCT(nome_cts, dados):
    ct = str(input("Digite o nome do CT exatamente igual ao CertPessoas: "))
    

    for i in range(len(nome_cts)):
        vagas = 0
        if ct in nome_cts[i]:
            print("CT: ", nome_cts[i])
            for j in range(len(dados[i])):
                vagas += int(dados[i][j][2])
            print(vagas)
    
    return


''' abertura, armazenamento e fechamento de arquivo'''
arquivo = abrir_arquivo()
dados = extrai_dados(arquivo)
fechar_arquivo(arquivo)

''' aqui extraio o tipo de exame'''
tipo_de_exame = (dados.pop(0))[7:]

''' removi as ocorrencias isoladas de \n'''
dados = list(filter(verificaBarraN, dados))

''' nome_cts = lista de strings
    dia_hora_vagas = lista de listas de triplas '''
nome_cts, dia_hora_vagas = formata_dados(dados)

#print(vagasTotaisPorMes('06',dia_hora_vagas))
print(dia_hora_vagas[0])
vagasPorUF(nome_cts, dia_hora_vagas)

#vagasPorCT(nome_cts, dia_hora_vagas)
