# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-30 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_homeimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeimage',
            name='alt',
        ),
        migrations.RemoveField(
            model_name='homeimage',
            name='created',
        ),
        migrations.RemoveField(
            model_name='homeimage',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='homeimage',
            name='thumb',
        ),
    ]
