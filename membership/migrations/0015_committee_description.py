# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0014_auto_20170318_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='description',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
