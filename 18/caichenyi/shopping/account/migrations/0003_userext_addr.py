# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userext_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='userext',
            name='addr',
            field=models.CharField(default='', max_length=256),
        ),
    ]
