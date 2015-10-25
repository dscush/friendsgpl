# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_auto_20151104_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='family_name_2',
            field=models.CharField(max_length=200, verbose_name='Alternative family name', blank=True),
        ),
    ]
