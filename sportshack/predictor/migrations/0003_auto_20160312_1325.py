# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 21:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_auto_20151129_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=datetime.datetime(2016, 3, 12, 21, 25, 48, 755001, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 3, 12, 13, 25, 6, 968244)),
        ),
    ]
