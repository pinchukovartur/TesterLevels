# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20171013_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsecretkey',
            name='title',
            field=models.CharField(default='null', max_length=10, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='levelfile',
            name='level_file',
            field=models.FileField(upload_to='levels/', verbose_name='File script'),
        ),
        migrations.AlterField(
            model_name='testsecretkey',
            name='secret_key',
            field=models.CharField(default='p6yweNKOZemFvQqbQasB7uNNFyF8nsME', max_length=32, verbose_name='Secret Key'),
        ),
    ]
