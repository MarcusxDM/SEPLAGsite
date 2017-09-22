# -*- coding: utf8 -*-

'''
Created on 20/09/2017

@author: Marcus Vinicius
'''
from BeautifulSoup import BeautifulSoup
from geopy.geocoders import Nominatim
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

def extractProduct(cartao):
    '''
    Recieves a block of product result from the HTML and saves the product objet
    '''
    #Django preparing object
    produto = Product()
    
    #Descricao
    descricao = cartao.b.string
    
    #Codigo do Produto
    codigoBarras = None
    if cartao.find('div', {'class' : 'bloco_descricao_img'}) is not None:
        codigoBarras = cartao.find('div', {'class' : 'bloco_descricao_img'})
        codigoBarras = str(codigoBarras.a.img['onclick'])
        codigoBarras = re.findall('\d+', codigoBarras)
        codigoBarras = str(codigoBarras[0])
    
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
    enderecoContribuinte = contribuinte.contents[2].string.replace('\n', '').replace('  ', ' ').replace('\r', '').replace('   ','')
    if enderecoContribuinte[0] == ' ':
        enderecoContribuinte = enderecoContribuinte.replace(' ', '', 1)
    
    #Bairro do Contribuinte
    bairroCepContribuinte = contribuinte.contents[4].string.replace('\n', '').replace('  ', '').replace('\r', '')
    bairroContribuinte    = charIntSplit(bairroCepContribuinte)
    #CEP do Contribuente
    if bairroCepContribuinte.count('.') >= 2:
        bairroCepContribuinte = bairroCepContribuinte.replace('.', '', 1)
    cepContribuinte       = bairroCepContribuinte.replace(bairroContribuinte, '').replace(',', '')
    
    #Latitude, Longitude e Razao Social
    if cartao.find('div', {'class' : 'bloco_contribuinte_img'}) is None:
        geolocator              = Nominatim()
        location                = geolocator.geocode(bairroContribuinte+" MACEIO")
        latitudeContribuinte    = location.latitude
        longitudeContribuinte   = location.longitude
        razaoSocialContribuinte = None
    else:
        cordenadas              = cartao.find('div', {'class' : 'bloco_contribuinte_img'}).a.img['onclick']
        cordenadas              = cordenadas.split('\'')
        latitudeContribuinte    = float(cordenadas[1])
        longitudeContribuinte   = float(cordenadas[3])
        razaoSocialContribuinte = cordenadas[5]
    
    print codigoBarras
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
    produto.productCode     = codigoBarras
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
    print "\n"
    
if __name__ == '__main__':
    #Opening HTML and turning it into BeautifulSoup object
    htmlSourceList = ['htmlsource/cerveja.html',
                      'htmlsource/sabonete.html', 
                      'htmlsource/macarrao.html',
                      'htmlsource/biscoito.html']
    
    for htmlDir in htmlSourceList:
        htmlSrc = codecs.open(htmlDir, 'r', encoding='utf-8')
        htmlSoup = BeautifulSoup(htmlSrc)
    
        #Finding product blocks in the HTML
        cartaoList = htmlSoup.findAll('div', {'class' : "cartao"})
        
        for cartao in cartaoList:
            extractProduct(cartao)
        
        htmlSrc.close()
        print "End of Extraction"
    
    