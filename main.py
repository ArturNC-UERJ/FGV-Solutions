import datetime as dt
from tkinter import *

#FUNÇÕES DE FORMATAÇÃO DO ARQUIVO
def extrai_dados():
	arquivo = open('03-03---04--09.txt', encoding='utf-8')

	#retorna lista iniciando por nome do exame e depois listas de cts
	lista = arquivo.readlines()

	arquivo.close()
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
			if ct != []:
				dia_hora_vagas.append(ct)
			ct = []
		elif arquivo[i][:4] == "Data":
			if len(arquivo[i]) == 42:
				ct.append((dt.datetime.strptime(arquivo[i][6:16] + " " + arquivo[i][25:30], '%d/%m/%Y %H:%M'), arquivo[i][-2]))
			elif len(arquivo[i]) == 43:
				ct.append((dt.datetime.strptime(arquivo[i][6:16] + " " + arquivo[i][25:30], '%d/%m/%Y %H:%M'), arquivo[i][-3:-1]))
			elif len(arquivo[i]) == 44:
				ct.append((dt.datetime.strptime(arquivo[i][6:16] + " " + arquivo[i][25:30], '%d/%m/%Y %H:%M'), arquivo[i][-4:-1]))

	dia_hora_vagas.append(ct)

	dados = [nomes_cts,dia_hora_vagas]

	return dados

def verificaBarraN(texto):
	if texto == "\n":
		return False
	else:
		return True

#FUNÇÕES DE OPERAÇÃO PRINCIPAIS
def detalhesCT(dados):

	print("Digite o nome do Centro de Testes: ")
	print("Dica: é possível digitar apenas partes do nome (Escreva igual ao certpessoas)")
	nomeCT = input()
	nomesCTS = []
	datasCTS = []

	for i in range(len(dados[0])):
		if nomeCT in dados[0][i]:
			nomesCTS.append(dados[0][i])
			datasCTS.append(dados[1][i])

	vagasPorPeriodo([nomesCTS,datasCTS])

	return

def vagasPorMes(dados):

	mes = int(input("Digite o mes: "))

	for i in range(len(dados[1])):
		print('-' * (len(dados[0][i]) + 4))
		print(f'| {dados[0][i]} |')
		print('-' * (len(dados[0][i]) + 4))
		print(f'|    DATA    | HORA  |VAGAS |')
		totVagas = 0
		for j in range(len(dados[1][i])):
			if dados[1][i][j][0].month == mes:
				totVagas += int(dados[1][i][j][1])
				print(
					f'| {dados[1][i][j][0]:%d}/{dados[1][i][j][0]:%m}/{dados[1][i][j][0]:%Y} | {dados[1][i][j][0]:%H}:{dados[1][i][j][0]:%M} |  {dados[1][i][j][1]:3} |')
		print('-' * (len('Total de vagas no período:    ') + 4))
		print(f'| Total de vagas no período: {totVagas} |')
		print('-' * (len('Total de vagas no período:    ') + 4))
		print()

	return

def vagasPorEstado(dados):
	UFs = ['AC','AL','AP','AM','BA','CE','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO','DF']

	vagas = 0

	print('Vagas por unidade federativa: ')
	for UF in UFs:
		for i in range(len(dados[0])):
			if dados[0][i][-2:] == UF:
				for j in range(len(dados[1][i])):
					vagas += int(dados[1][i][j][1])
		print("{} --> {}".format(UF, vagas))
		vagas = 0

	return

def vagasPorPeriodo(dados):

	diaI = int(input("Digite o dia inicial do intervalo: "))
	mesI = int(input("Digite o mes inicial do intervalo: "))
	anoI = int(input("Digite o ano inicial do intervalo: "))

	diaF = int(input("Digite o dia final do intervalo: "))
	mesF = int(input("Digite o mes final do intervalo: "))
	anoF = int(input("Digite o ano final do intervalo: "))

	inicio = dt.datetime(anoI, mesI, diaI)
	final = dt.datetime(anoF, mesF, diaF+1) #+1 pq tava dando erro foda-se

	for i in range(len(dados[1])):
		print('-'*(len(dados[0][i]) + 4))
		print(f'| {dados[0][i]} |')
		print('-' * (len(dados[0][i]) + 4))
		print(f'|    DATA    | HORA  |VAGAS |')
		totVagas = 0
		for j in range(len(dados[1][i])):
			if inicio <= dados[1][i][j][0] <= final:
				totVagas += int(dados[1][i][j][1])
				print(f'| {dados[1][i][j][0]:%d}/{dados[1][i][j][0]:%m}/{dados[1][i][j][0]:%Y} | {dados[1][i][j][0]:%H}:{dados[1][i][j][0]:%M} |  {dados[1][i][j][1]:3} |')
		print('-' * (len('Total de vagas no período:    ') + 4))
		print(f'| Total de vagas no período: {totVagas} |')
		print('-' * (len('Total de vagas no período:    ') + 4))
		print()

	return

if __name__ == '__main__':

	# abertura, armazenamento e fechamento de arquivo
	dados = extrai_dados()

	# aqui extraio o tipo de exame
	tipo_de_exame = (dados.pop(0))[7:]

	# removi as ocorrencias isoladas de \n
	dados = list(filter(verificaBarraN, dados))

	# dados[0] = lista de nomes de cts
	# dados[1] = lista de listas de tuplas | ex: [[(datetime,vagas)],[(datetime,vagas)],[(datetime,vagas)]]
	dados_form = formata_dados(dados)

	#vagasPorEstado(dados_form)
	#vagasPorPeriodo(dados_form)
	#vagasPorMes(dados_form)
	#detalhesCT(dados_form)
