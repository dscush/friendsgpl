# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 22:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0011_auto_20170318_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='board',
            new_name='role',
        ),
    ]
