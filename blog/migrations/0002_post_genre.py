# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-19 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default='Kurzgeschichten', max_length=200),
            preserve_default=False,
        ),
    ]