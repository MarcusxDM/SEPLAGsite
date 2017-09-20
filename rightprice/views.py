# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import loader


def index(request):
    product_list = Product.objects.all()
    template = loader.get_template('rightprice/index.html')
    context = {
            'product_list': product_list,
    }
    #output = ', '.join([p.description for p in product_list])
    return HttpResponse(template.render(context, request))