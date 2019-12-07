import requests
import json
import pandas

def converter_data(dia):
    dia = dia[8:]+'/'+dia[5:7]+'/'+dia[0:4]
    print("Última atualização dos dados: ", dia)
    return dia

def chave_acesso(chave='90c3ad3e6267b1af2d246b245076f858&'):
    return 'http://data.fixer.io/api/latest?access_key='+chave

def converter_em_reais(valor_real, valor_estrangeiro):
    return round(valor_real/valor_estrangeiro, 2)

def exportar_tabela(lista_titulos, lista_valores, nome_arquivo, lista_dia):
    celulas = pandas.DataFrame({'Moedas':lista_titulos,
                              'Valores':lista_valores,
                              'Acessado em':lista_dia}) 
    celulas.to_csv(nome_arquivo+'.csv',index=False, sep=';')
    print("Tabela exportada com sucesso!!!!")
   

 # adcionado pra transformar os dados em dicionario
# Utilizamos a função get do requests para acessar o servidor da API onde se encontra as
# infomações das moedas.
# Ao acesar o servidor, a variável status_code, do requests, é preenchida com a resposta HTTP do servidor.
# E a variável content, támbem do requests, é preenchida com o conteúdo da API(JSON)
#Utilizamos a biblioteca Json, para converter os dados recebidos em um dicionario
#
chave = input("Informe a chave de acesso do Fixer.io, se não tiver, aperte enter :")
url = chave_acesso(chave) if len(chave) > 0 else chave_acesso()
print("Acessando base de dados...")
resposta = requests.get(url)#Requisição a uma pagina web
if resposta.status_code == 200:#resposta fica variavel status code, vai trazer a lista de varios conteudos(acessar o conteudo)
    print('conexão com a Base de Dados, estabelecida com sucesso')
    print(resposta.content)
    dados = resposta.json()#acessando o conteudo que veio em resposta, atribuindo a varieval dados( atribuindo a a variavel dados)
    #A função converter_data irá receber o valor da variavel dados['date'] e irá
    #retornar a data convertida no padrão Brasil, que será atribuida a variável
    #dia_convertido
    dia_convertido = converter_data(dados['date'])
    euro_em_reais = converter_em_reais(dados['rates']['BRL'], dados['rates']['EUR'])#round arrendondar as casas decimansi apois da virgula
    bitcoin_em_reais = converter_em_reais(dados ['rates']['BRL'], dados['rates']['BTC'])
    dolar_em_reais = converter_em_reais(dados ['rates']['BRL'], dados['rates']['USD'])
    
    escolha = input('Digite:\nB - Bitcoin\nD - Dollar\nE - Euro\nA - Todas\n').upper()
    if (escolha == 'B'):
        exportar_tabela(['Bitcoin'], [bitcoin_em_reais], 'bitcoin', [dia_convertido])
    elif(escolha =='D'):
        exportar_tabela(['Dollar'], [dolar_em_reais], 'dollar', [dia_convertido])
    elif(escolha =='E'):
        exportar_tabela(['Euro'], [euro_em_reais], 'euro', [dia_convertido])
    elif(escolha =='A'):
        exportar_tabela(['Bitcoin', 'Dollar', 'Euro'], [bitcoin_em_reais, dolar_em_reais, euro_em_reais],
                        'moedas', [dia_convertido, '', ''])
    else:
        print('Você não escolheu nenhuma das opções. Sua tabela será exportada!')
else:
    print('Erro ao acessar o base de dados')

                              
                              #adcionando biblioteca pandas
                                # Chaves cria dicionario em seguidas criar lista #
                                # ( No pandas a chave do dicionario é o titulo da coluna e a lista é o conteudo da coluna. Precisa import pandas)



