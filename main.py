#Vamos realizar as seguintes operações:
# 1) Extração do conteúdo do site
# 2) Tratamento do conteúdo extraído
# 3) Converter as informações em um arquivo CSV

#Bibliotecas que serão utilizadas
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import csv

# Acessando o site

site_exame = 'https://exame.com/negocios/quais-serao-os-proximos-unicornios-de-2023-veja-lista/'

try:
  conteudo = requests.get(site_exame)
  conteudo.raise_for_status()
except HTTPError as exc:
  print(exc)
else:
  conteudo_exame = conteudo.text
  conteudo_decodificado = conteudo.apparent_encoding
  conteudo_site = conteudo.content.decode(conteudo_decodificado)

# Extraindo o conteúdo da página
pagina = BeautifulSoup(conteudo_site, 'html.parser')

tabela = pagina.find(class_= 'sc-1b218489-4 idAAkB')
conteudo_extraido = []

for linha in tabela.find_all('tr'):
  textos_coluna = list()
  for coluna in linha.find_all('td'):
    texto_coluna = coluna.get_text().strip().split('\n')
    textos_coluna += texto_coluna
    conteudo_extraido.append(texto_coluna)

# Tratando as informações

ranking = []
nome = []
ramo = []

#RANKING
comeco = 0

for i in range(0, 51):
  ranking.append(conteudo_extraido[comeco])
  comeco = comeco + 3
  i = i + 1

#NOME
comeco = 1

for i in range(0, 51):
  nome.append(conteudo_extraido[comeco])
  comeco = comeco + 3
  i = i + 1

#RAMO
comeco = 2

for i in range(0, 51):
  ramo.append(conteudo_extraido[comeco])
  comeco = comeco + 3
  i = i + 1

#Vamos agora, transportar as informações para um arquivo CSV: Lista_Completa.csv

with open(file='Lista_Completa.csv', mode='w', encoding='utf8') as arquivo:
  escritor_csv = csv.writer(arquivo, delimiter=';')

  for i in range(0, len(ranking)):
    rank = str(ranking).replace("'"," " ).replace('[', ' ').replace(']', ' ').split(sep=',')
    name = str(nome).replace("'"," " ).replace('[', ' ').replace(']', ' ').split(sep=',')
    setor = str(ramo).replace("'"," " ).replace('[', ' ').replace(']', ' ').split(sep=',')

    escritor_csv.writerow([rank[i], name[i], setor[i]])
    i = i+1
  
  arquivo.close()