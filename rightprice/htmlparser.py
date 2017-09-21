# -*- coding: utf8 -*-

'''
Created on 20/09/2017

@author: Marcus Vinicius
'''
from BeautifulSoup import BeautifulSoup
import codecs
import re

def precoNormalizer(string):
    string = string.replace('R', '').replace('$', ''). replace(' ', ''). replace(',', '.')
    precoFloat = float(string)
    return precoFloat

def charIntSplit(string):
    i = 0
    string = re.findall(r"[^\W\d_]+|\d+", string)
    stringFinal = string[0]
    while re.search('[a-zA-Z]', string[i+1]):
            stringFinal = stringFinal+' '+string[i+1]
            i = i+1
    return stringFinal
    
htmlSrc = codecs.open("htmlsource/cerveja.html", 'r', encoding='utf-8')
#print htmlSrc.read()
htmlSoup = BeautifulSoup(htmlSrc)
#print htmlSoup.prettify()

#Encontrar comeco de Produto
cartao = htmlSoup.find('div', {'class' : "cartao"})

#Descricao
description = cartao.b.string

#Preco Maximo
precoMax = cartao.find('span', {'style' : 'color: #B71C1C; text-align: right;'})
precoMaxString = precoMax.contents[0].string
precoMaxFloat = precoNormalizer(precoMaxString)

#Preco Minimo
precoMin = cartao.find('span', {'style' : 'color: #1B5E20; text-align: right;'})
precoMinString = precoMin.contents[0].string
precoMinFloat = precoNormalizer(precoMinString)

#Contribuinte
contribuinte = cartao.find('div', {'class' : 'bloco_contribuinte_endereco'})
#Nome do Contribuinte
nomeContribuinte = contribuinte.contents[0].string.replace('\n', '').replace('  ', '').replace('\r', '')
#Endereco do Contribuente
enderecoContribuinte = contribuinte.contents[2].string.replace('\n', '').replace('  ', '').replace('\r', '')
#Bairro do Contribuinte
bairroCepContribuinte = contribuinte.contents[4].string.replace('\n', '').replace('  ', '').replace('\r', '')
bairroContribuinte = charIntSplit(bairroCepContribuinte)
#CEP do Contribuente
cepContribuinte = bairroCepContribuinte.replace(bairroContribuinte, '').replace(',', '')

#Longitude e Latitude
cordenadas = cartao.find('div', {'class' : 'bloco_contribuinte_img'}).a.img['onclick']
print description
print precoMaxFloat
print precoMinFloat
print nomeContribuinte
print enderecoContribuinte
print bairroContribuinte
print cepContribuinte
print cordenadas

htmlSrc.close()