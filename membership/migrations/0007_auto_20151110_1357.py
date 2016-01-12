# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_member_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='board',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='trustee',
            field=models.BooleanField(default=False),
        ),
    ]
