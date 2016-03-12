# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('game_id', models.IntegerField()),
                ('home_team', models.CharField(max_length=255)),
                ('away_team', models.CharField(max_length=255)),
                ('home_score', models.IntegerField()),
                ('away_score', models.IntegerField()),
                ('home_qt1', models.IntegerField()),
                ('home_qt2', models.IntegerField()),
                ('home_qt3', models.IntegerField()),
                ('home_qt4', models.IntegerField()),
                ('away_qt1', models.IntegerField()),
                ('away_qt2', models.IntegerField()),
                ('away_qt3', models.IntegerField()),
                ('away_qt4', models.IntegerField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2015, 11, 29, 7, 18, 13, 49051))),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type_id', models.CharField(max_length=255)),
                ('success', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('team', models.CharField(max_length=255)),
                ('touchdown', models.IntegerField()),
                ('points', models.IntegerField()),
                ('fumbles', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=7, max_digits=10)),
                ('weight', models.IntegerField()),
                ('birthplace', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('award_points', models.IntegerField()),
                ('play', models.ForeignKey(to='predictor.Play')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('win', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('points', models.IntegerField()),
                ('points_scored', models.IntegerField()),
                ('points_conceded', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('num_votes', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
