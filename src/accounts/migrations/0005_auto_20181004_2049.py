# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-04 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181004_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True),
        ),
    ]
