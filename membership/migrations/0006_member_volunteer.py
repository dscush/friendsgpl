# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_family_family_name_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='volunteer',
            field=models.BooleanField(default=False),
        ),
    ]
