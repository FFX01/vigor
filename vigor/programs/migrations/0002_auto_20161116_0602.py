# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.CharField(default='n/a', max_length=200),
        ),
    ]