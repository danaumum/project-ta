# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-25 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0013_auto_20180925_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bangunan_corong',
            name='foto',
            field=models.ImageField(blank=True, default='noPic.png', upload_to=''),
        ),
    ]
