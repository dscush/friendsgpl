# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CMSBlock',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
    ]
