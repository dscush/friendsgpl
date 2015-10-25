# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20151104_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='street_address1',
            new_name='street_address_1',
        ),
        migrations.RenameField(
            model_name='family',
            old_name='street_address2',
            new_name='street_address_2',
        ),
    ]
