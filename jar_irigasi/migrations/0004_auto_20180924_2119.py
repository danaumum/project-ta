# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-24 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0003_bangunan_sadap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangunan_sadap',
            name='letak',
        ),
        migrations.RemoveField(
            model_name='bangunan_sadap',
            name='slug',
        ),
        migrations.AddField(
            model_name='bangunan_sadap',
            name='foto',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
