# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-21 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0005_shows_theme'),
        ('l_r_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='show',
            field=models.ManyToManyField(related_name='users', to='shows_app.shows'),
        ),
    ]
