# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-30 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190929_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='homeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=b'albums')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to=b'albums')),
                ('alt', models.CharField(default=uuid.uuid4, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('caption', models.TextField(max_length=200)),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=70)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Album')),
            ],
        ),
    ]
