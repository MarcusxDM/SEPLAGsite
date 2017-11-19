# -*- coding: utf-8 -*-
'''

Google Maps API Key: AIzaSyApMGZ2UbGB5OjHub7QCffJEjmI2jHIb0Y

@author: Marcus Vinicius
'''
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Product
from django.template import loader
from django.shortcuts import render_to_response
from templatetags.rightprice_extras import jsonify
from rightprice.models import Store

def index(request):
    store_list = Store.objects.all()
    template = loader.get_template('rightprice/index.html')
    context = {
            'store_list': store_list,
    }
    #output = ', '.join([p.description for p in product_list])
    return HttpResponse(template.render(context, request))

"""def indexJSON(request):
    product_list = Product.objects.all().values_list('fantasiaName')
    template = loader.get_template('rightprice/index.html')
    context = {
            'product_list': product_list,
    }
    #output = ', '.join([p.description for p in product_list])
    prices_json = json.dumps(list(product_list), cls=DjangoJSONEncoder)
    return HttpResponse(template.render(context, request))"""

def detail(request, product_id):
    # Our query is ready to take off.
    productResult = Product.objects.get(
        id=product_id,
    )
    return render_to_response('product_info.html', {'product':productResult})

def search(request):
    # Suppose we support these params -> ('director', 'fromdate', 'todate')
    request_params = request.GET.copy()
    # Our query is ready to take off.
    dscrp = request_params['description']
    fanta = request_params['fantasiaName']
    neigh = request_params['neighborhood']
    
    #None
    if dscrp is None and fanta is None and neigh == 'all':
        productResults = Product.objects.all()
    
    #All
    if dscrp is not None and fanta is not None and neigh != 'all':
        productResults = Product.objects.filter(
           description__icontains=request_params['description'],
           fantasiaName__icontains=request_params['fantasiaName'],
           neighborhood__icontains=request_params['neighborhood'])
    
    #Description
    if dscrp is not None and fanta is None and neigh != 'all':
        productResults = Product.objects.filter(
           description__icontains=request_params['description'],
           neighborhood__icontains=request_params['neighborhood']) 
    
    if dscrp is not None and fanta is not None and neigh == 'all':
        productResults = Product.objects.filter(
           description__icontains=request_params['description'],
           fantasiaName__icontains=request_params['fantasiaName'])
    
    if dscrp is not None and fanta is None and neigh == 'all':
        productResults = Product.objects.filter(
           description__icontains=request_params['description'])
        
    #Fantasia
    if dscrp is None and fanta is not None and neigh != 'all':
        productResults = Product.objects.filter(
           fantasiaName__icontains=request_params['fantasiaName'],
           neighborhood__icontains=request_params['neighborhood']) 
    
    if dscrp is None and fanta is not None and neigh == 'all':
        productResults = Product.objects.filter(
           fantasiaName__icontains=request_params['fantasiaName'])   
    
         
    
    return render_to_response('search_results.html', {'results':productResults})


