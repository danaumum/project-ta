# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-19 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0032_auto_20181019_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangunan_corong',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='bangunan_corong',
            name='longitude',
        ),
    ]
