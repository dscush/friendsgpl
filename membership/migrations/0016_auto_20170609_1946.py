# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0015_committee_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membership.Member'),
        ),
    ]
