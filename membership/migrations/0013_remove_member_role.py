# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0012_auto_20170318_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='role',
        ),
    ]
