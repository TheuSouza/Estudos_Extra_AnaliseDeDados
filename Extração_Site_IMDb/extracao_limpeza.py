import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import csv


pagina = None
conteudo = None
url = 'https://www.imdb.com/chart/top/'

dados = list()
conteudo_extraido = list()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

try:
    resposta = requests.get(url, headers=headers)
    resposta.raise_for_status()
    pagina = resposta.content
except HTTPError as error:
    print(error)

soup = BeautifulSoup(pagina, 'html.parser')

for linha in soup.find_all('div', class_='sc-b0691f29-0 jbYPfh cli-children'):
   conteudo = linha.get_text(';').strip().split(';')
   conteudo = conteudo[0].split('.') + conteudo[1:5]
   conteudo_extraido.append(conteudo)

del conteudo_extraido[162][1:4]
conteudo_extraido[199][1] += conteudo_extraido[199][2]
del conteudo_extraido[199][2:4]
conteudo_extraido[209][1] += conteudo_extraido[209][2]
del conteudo_extraido[209][2]
conteudo_extraido[71][1] += conteudo_extraido[71][2]
del conteudo_extraido[71][2]
del conteudo_extraido[57][5]
conteudo_extraido[57].insert(4,'Not Rated')

for linha in conteudo_extraido:
    linha[1] = linha[1].strip()

with open(file='./IMDb.csv', mode='w', encoding='utf-8') as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=';')
    arquivo_csv.writerows([['Ranking','Titulo','Ano','Duração','Classificação','Avaliação']]
                           + list(map(lambda linha: linha, conteudo_extraido)))

    