# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0016_auto_20170404_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='date_paid',
            field=models.DateField(),
        ),
    ]
