# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-24 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangunan_corong',
            name='foto',
        ),
    ]
