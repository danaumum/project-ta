# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-24 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0006_bangunan_sadap_letak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bangunan_sadap',
            name='letak',
            field=models.CharField(max_length=50),
        ),
    ]
