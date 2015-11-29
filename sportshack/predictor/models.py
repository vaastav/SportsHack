from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

MAX_LENGTH = 255
DECIMAL_PLACES = 7
MAX_DIGITS = DECIMAL_PLACES + 4

class Game(models.Model):
  home_team = models.CharField(max_length = MAX_LENGTH)
  away_team = models.CharField(max_length = MAX_LENGTH)
  home_score = models.IntegerField()
  away_score = models.IntegerField()
  home_score_qt1 = models.IntegerField()
  home_score_qt2 = models.IntegerField()
  home_score_qt3 = models.IntegerField()
  home_score_qt4 = models.IntegerField()
  away_score_qt1 = models.IntegerField()
  away_score_qt2 = models.IntegerField()
  away_score_qt3 = models.IntegerField()
  away_score_qt4 = models.IntegerField()
  home_touchdowns = models.IntegerField()
  away_touchdowns = models.IntegerField()
  home_field_goals = models.IntegerField()
  away_field_goals = models.IntegerField()

class Team(models.Model):
  name = models.CharField(max_length = MAX_LENGTH)
  win = models.IntegerField()
  loss = models.IntegerField()
  win_ot = models.IntegerField()
  loss_ot = models.IntegerField()
  points = models.IntegerField()
  points_scored = models.IntegerField()
  points_conceded = models.IntegerField() 

class Player(models.Model):
  first_name = models.CharField(max_length = MAX_LENGTH)
  last_name = models.CharField(max_length = MAX_LENGTH)
  team = models.ForeignKey(Team)
  touchdown = models.IntegerField()
  points = models.IntegerField()
  fumbles = models.IntegerField()
  height = models.DecimalField(max_digits = MAX_DIGITS, decimal_places = DECIMAL_PLACES)
  weight = models.IntegerField()
  birthplace = models.CharField(max_length = MAX_LENGTH)
  birthdate = models.DateTimeField()

class Play(models.Model):
  type_id = models.CharField(max_length = MAX_LENGTH)
  success = models.IntegerField()

class Predictions(models.Model):
  play = models.ForeignKey(Play)
#  user = models.ForeignKey(User)
  award_points = models.IntegerField()
