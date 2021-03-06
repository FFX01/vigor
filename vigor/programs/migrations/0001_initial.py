# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 05:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('styles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=1)),
                ('sets', models.PositiveIntegerField(blank=True, default=1)),
                ('weight', models.PositiveIntegerField(blank=True, default=1)),
                ('duration', models.PositiveIntegerField(blank=True, default=1)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('followers', models.ManyToManyField(related_name='programs', to=settings.AUTH_USER_MODEL)),
                ('maintainers', models.ManyToManyField(related_name='maintained_programs', to=settings.AUTH_USER_MODEL)),
                ('styles', models.ManyToManyField(related_name='programs', to='styles.Style')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1)),
                ('description', models.TextField()),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='programs.Period')),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periods', to='programs.Program'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='programs.Session'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='styles',
            field=models.ManyToManyField(related_name='exercises', to='styles.Style'),
        ),
    ]
