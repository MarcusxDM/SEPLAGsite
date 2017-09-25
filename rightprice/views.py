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


def index(request):
    product_list = Product.objects.all()
    template = loader.get_template('rightprice/index.html')
    context = {
            'product_list': product_list,
    }
    #output = ', '.join([p.description for p in product_list])
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    return HttpResponse("Product ID: %s." % product_id)

def search(request):
    # Suppose we support these params -> ('director', 'fromdate', 'todate')
    request_params = request.GET.copy()
    # Our query is ready to take off.
    productResults = Product.objects.filter(
        description__icontains=request_params['description'],
    )
    return render_to_response('search_results.html', {'results':productResults})