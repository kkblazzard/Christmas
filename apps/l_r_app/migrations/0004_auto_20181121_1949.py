# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-21 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l_r_app', '0003_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
