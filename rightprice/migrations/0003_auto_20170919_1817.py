# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rightprice', '0002_auto_20170919_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='LastSellPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='lastSellPriceU',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='latitudeNum',
            field=models.DecimalField(blank=True, decimal_places=100, max_digits=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='longitudeNum',
            field=models.DecimalField(blank=True, decimal_places=100, max_digits=200, null=True),
        ),
    ]
