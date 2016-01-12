# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0007_auto_20151110_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='comment',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='street_address_1',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
