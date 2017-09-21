# -*- coding: utf8 -*-

'''
Created on 20/09/2017

@author: Marcus Vinicius
'''
from BeautifulSoup import BeautifulSoup
import codecs
import re
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'SEPLAGsite.settings'

import django
django.setup()

from rightprice.models import Product

def precoNormalizer(string):
    '''
    Recieves a string, deletes all alphanumeric characters and turn it into
    a float type, then, returning the float object
    '''
    string = string.replace('R', '').replace('$', ''). replace(' ', ''). replace(',', '.')
    precoFloat = float(string)
    return precoFloat

def charIntSplit(string):
    '''
    Recieves a string(Neighborhood+CEP) and splits it, removing the CEP
    and then returns only the Neighborhood string
    '''
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

#Django preparing object
produto = Product()

#Encontrar comeco de Produto
cartao = htmlSoup.find('div', {'class' : "cartao"})

#Descricao
descricao = str(cartao.b.string)

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
nomeContribuinte = str(contribuinte.contents[0].string.replace('\n', '').replace('  ', '').replace('\r', ''))
#Endereco do Contribuente
enderecoContribuinte = str(contribuinte.contents[2].string.replace('\n', '').replace('  ', '').replace('\r', ''))
#Bairro do Contribuinte
bairroCepContribuinte = str(contribuinte.contents[4].string.replace('\n', '').replace('  ', '').replace('\r', ''))
bairroContribuinte = str(charIntSplit(bairroCepContribuinte))
#CEP do Contribuente
cepContribuinte = str(bairroCepContribuinte.replace(bairroContribuinte, '').replace(',', ''))
#Latitude, Longitude e Razao Social
cordenadas = str(cartao.find('div', {'class' : 'bloco_contribuinte_img'}).a.img['onclick'])
cordenadas = cordenadas.split('\'')
latitudeContribuinte = float(cordenadas[1])
longitudeContribuinte = float(cordenadas[3])
razaoSocialContribuinte = str(cordenadas[5])

print descricao
print precoMaxFloat
print precoMinFloat
print nomeContribuinte
print enderecoContribuinte
print bairroContribuinte
print cepContribuinte
print latitudeContribuinte  
print longitudeContribuinte
print razaoSocialContribuinte

#
produto.description     = descricao
produto.SellPriceMax    = precoMaxFloat
produto.SellPriceMin    = precoMinFloat
produto.fantasiaName    = nomeContribuinte
produto.addressName     = enderecoContribuinte
produto.neighborhood    = bairroContribuinte
produto.cepNum          = cepContribuinte
produto.latitudeNum     = latitudeContribuinte
produto.longitudeNum    = longitudeContribuinte
produto.razaoSocialName = razaoSocialContribuinte
produto.cityName        = "MACEIÓ"
produto.save()

htmlSrc.close()