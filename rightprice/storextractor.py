# -*- coding: utf8 -*-

'''
Created on 24/09/2017

@author: Marcus Vinicius
'''
import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'SEPLAGsite.settings'

import django
django.setup()

from rightprice.models import Product, Store

def storeXtractor(productList):
    for product in productList:
        fantasiaList = Store.objects.values_list('fantasiaName', flat=True).distinct()
        if product.fantasiaName not in fantasiaList:
            print product.fantasiaName+'\n'
            store = Store()
            store.fantasiaName    = product.fantasiaName
            store.addressName     = product.addressName
            store.neighborhood    = product.neighborhood
            store.cepNum          = product.cepNum
            store.latitudeNum     = product.latitudeNum
            store.longitudeNum    = product.longitudeNum
            store.razaoSocialName = product.razaoSocialName
            store.cityName        = "MACEIÓ"
            store.save()
            print "Store saved\n###########\n"
    print "Extraction finished"

if __name__ == '__main__':
    product = Product()
    
    productList = Product.objects.all()
    
    storeXtractor(productList)
            
            
            