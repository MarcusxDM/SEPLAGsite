# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productCode', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('lastSellDate', models.CharField(max_length=200)),
                ('dataLastEmitTxt', models.CharField(max_length=200)),
                ('cnpjNum', models.CharField(max_length=200)),
                ('razaoSocialName', models.CharField(max_length=200)),
                ('fantasiaName', models.CharField(max_length=200)),
                ('telephoneNum', models.CharField(max_length=200)),
                ('streetName', models.CharField(max_length=200)),
                ('placeNum', models.CharField(max_length=200)),
                ('neighborhood', models.CharField(max_length=200)),
                ('cepNum', models.CharField(max_length=200)),
                ('cityName', models.CharField(max_length=200)),
            ],
        ),
    ]
