# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-03 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20191002_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumimage',
            name='commenter',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='alt',
            field=models.CharField(max_length=255),
        ),
    ]
