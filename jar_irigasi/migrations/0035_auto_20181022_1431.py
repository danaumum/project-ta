# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-22 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jar_irigasi', '0034_auto_20181019_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangunan_bendung',
            name='foto',
        ),
        migrations.AddField(
            model_name='bangunan_bendung',
            name='foto1',
            field=models.ImageField(blank=True, default='noPic.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='bangunan_bendung',
            name='foto2',
            field=models.ImageField(blank=True, default='noPic.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='bangunan_bendung',
            name='foto3',
            field=models.ImageField(blank=True, default='noPic.png', upload_to=''),
        ),
    ]