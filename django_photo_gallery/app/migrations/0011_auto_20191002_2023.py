# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-02 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190930_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumimage',
            name='comment',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='date',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='place',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='caption',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
