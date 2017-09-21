# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

    
@python_2_unicode_compatible    
class Product(models.Model):
    def __str__(self):
        return self.description
    
    productCode = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    SellPriceMax = models.DecimalField(max_digits=200, decimal_places=2, null=True, blank=True)
    SellPriceMin = models.DecimalField(max_digits=200, decimal_places=2, null=True, blank=True)
    razaoSocialName = models.CharField(max_length=200)
    fantasiaName = models.CharField(max_length=200)
    addressName = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    cepNum = models.CharField(max_length=200)
    cityName = models.CharField(max_length=200)
    latitudeNum = models.DecimalField(max_digits=200, decimal_places=7, null=True, blank=True)
    longitudeNum = models.DecimalField(max_digits=200, decimal_places=7, null=True, blank=True)
