# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 21:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0003_auto_20160312_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 3, 12, 13, 25, 55, 862784)),
        ),
    ]