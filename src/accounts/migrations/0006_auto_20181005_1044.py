# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-05 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181004_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ngo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
    ]
