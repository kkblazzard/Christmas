# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-20 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0003_auto_20181120_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='image',
            field=models.URLField(default='http', max_length=1250),
            preserve_default=False,
        ),
    ]
