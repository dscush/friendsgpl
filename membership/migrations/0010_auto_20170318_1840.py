# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0009_auto_20170318_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='board',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
