# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-22 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0036_auto_20181022_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangunan_sadap',
            name='foto',
        ),
        migrations.AddField(
            model_name='bangunan_sadap',
            name='foto1',
            field=models.ImageField(blank=True, default='noPic.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='bangunan_sadap',
            name='foto2',
            field=models.ImageField(blank=True, default='noPic.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='bangunan_sadap',
            name='foto3',
            field=models.ImageField(blank=True, default='noPic.png', upload_to=''),
        ),
    ]
