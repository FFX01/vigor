# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markupfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', markupfield.fields.MarkupField(rendered_field=True)),
                ('description_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown')], default='markdown', editable=False, max_length=30)),
                ('_description_rendered', models.TextField(editable=False)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplines.Discipline')),
            ],
        ),
    ]