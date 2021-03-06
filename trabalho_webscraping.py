# -*- coding: utf-8 -*-
"""trabalho_webscraping

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y8vdM2z3GFTZ-1WUOaH0nXxfmmjscnLi

#Raspagem do Portal de Notícias da FUNARTE
https://antigo.funarte.gov.br/noticias/
"""

!pip install requests
!pip install beautifulsoup4

import requests
url = "https://antigo.funarte.gov.br/noticias/"
resposta = requests.get(url)
html = resposta.text

from bs4 import BeautifulSoup

print(html)

print(resposta.headers) #printou o cabeçado com atributos sobre o servidor que hospeda o site

def extrair_dados(): 
  response = requests.get("https://antigo.funarte.gov.br/noticias/")
  html = BeautifulSoup(response.text,"html.parser")
  secao_noticias = html.find('section', {'class': 'box-news'}) #isola ou encontra a secao no html em que as notícias estão 
  noticias = secao_noticias.find_all('li') #isola, a partir da tag ''li'', o local em que as notícias estão contidas>> find_all me devolve uma lista de todas as notícias
  
  resultado = [] # criou lista para guardar os resultados
  for noticia in noticias:
        titulo = noticia.find('h3').text #isola o título a partir da identificação da tag "h3", que o precede
        link = noticia.find('a').attrs['href'] #isola o link a partir da identificação da tag "href", que o precede
        resultado.append({'titulo': titulo.strip(), 'link': link}) # inseriu minhas informações, em formato de dicionário, dentro da lista
  return resultado

"""Criando uma tabela para importar os dados em formato csv"""

import pandas as pd

lista_noticias = extrair_dados()
dados = pd.DataFrame(lista_noticias, columns=['titulo', 'link'])
dados.to_excel('noticias.xlsx', index=False)
print(dados)