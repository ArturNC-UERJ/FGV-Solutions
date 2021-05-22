def abrir_arquivo():
	arquivo = open('dados/03-03---04--09.txt', encoding='utf-8')
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


def vagasPorMes(mes, dados):
	vagas = 0

	for i in dados:
		for x in i:
			if x[0][3:5] == mes:
				vagas += int(x[2])

	return vagas


#abertura, armazenamento e fechamento de arquivo
arquivo = abrir_arquivo()
dados = extrai_dados(arquivo)
fechar_arquivo(arquivo)

#aqui extraio o tipo de exame
tipo_de_exame = (dados.pop(0))[7:]

#removi as ocorrencias isoladas de \n
dados = list(filter(verificaBarraN, dados))

#nome_cts = lista de strings
#dia_hora_vagas = lista de listas de triplas
nome_cts, dia_hora_vagas = formata_dados(dados)

print(vagasPorMes('04', dia_hora_vagas))
