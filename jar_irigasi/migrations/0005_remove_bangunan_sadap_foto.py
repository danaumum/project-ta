# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-24 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0004_auto_20180924_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangunan_sadap',
            name='foto',
        ),
    ]
