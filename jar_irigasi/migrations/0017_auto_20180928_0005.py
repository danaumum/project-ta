# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-27 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0016_auto_20180928_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bangunan_corong',
            name='debit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bangunan_corong',
            name='luas_terairi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bangunan_sadap',
            name='debit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bangunan_sadap',
            name='luas_terairi',
            field=models.IntegerField(),
        ),
    ]
