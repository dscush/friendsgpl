# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20151025_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='zip_code',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\d{5}$', message='Please enter a five-digit ZIP code.')], max_length=5),
        ),
    ]
