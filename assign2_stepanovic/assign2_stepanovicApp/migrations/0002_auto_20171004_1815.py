# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign2_stepanovicApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='state',
            field=models.CharField(default='Active', max_length=15),
        ),
    ]
