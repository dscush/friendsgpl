# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('family_name', models.CharField(max_length=200)),
                ('street_address1', models.CharField(max_length=200)),
                ('street_address2', models.CharField(blank=True, max_length=200)),
                ('zip_code', models.IntegerField(validators=[django.core.validators.RegexValidator(regex='^\\d{5}$', message='Please enter a five-digit ZIP code.')])),
                ('home_phone', models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$', message='Please enter a ten-digit phone number.')], null=True)),
                ('last_paid', models.DateField(verbose_name='date dues paid')),
                ('dues_amount', models.PositiveSmallIntegerField()),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator()], null=True)),
                ('personal_phone', models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$', message='Please enter a ten-digit phone number.')], null=True)),
                ('family', models.ForeignKey(to='membership.Family')),
            ],
        ),
    ]
