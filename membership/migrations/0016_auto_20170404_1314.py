# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 17:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0015_committee_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='dues_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='family',
            old_name='last_paid',
            new_name='date_paid',
        ),
    ]
