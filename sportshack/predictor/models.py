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
  home_qt1 = models.IntegerField()
  home_qt2 = models.IntegerField()
  home_qt3 = models.IntegerField()
  home_qt4 = models.IntegerField()
  away_qt1 = models.IntegerField()
  away_qt2 = models.IntegerField()
  away_qt3 = models.IntegerField()
  away_qt4 = models.IntegerField()
  date = models.DateTimeField(default=datetime.date.today)

class Team(models.Model):
  name = models.CharField(max_length = MAX_LENGTH)
  win = models.IntegerField()
  loss = models.IntegerField()
  points = models.IntegerField()
  points_scored = models.IntegerField()
  points_conceded = models.IntegerField() 

class User(models.Model):
  user = models.OneToOneField(User, null=True)
  points = models.IntegerField()
  num_votes = models.IntegerField()
  
class Player(models.Model):
  first_name = models.CharField(max_length = MAX_LENGTH)
  last_name = models.CharField(max_length = MAX_LENGTH)
  team = models.CharField(max_length = MAX_LENGTH)
  touchdown = models.IntegerField()
  points = models.IntegerField()
  fumbles = models.IntegerField()
  height = models.DecimalField(max_digits = MAX_DIGITS, decimal_places = DECIMAL_PLACES)
  weight = models.IntegerField()
  birthplace = models.CharField(max_length = MAX_LENGTH)
  position = models.CharField(max_length = MAX_LENGTH)

class Play(models.Model):
  type_id = models.CharField(max_length = MAX_LENGTH)
  success = models.IntegerField()

class Predictions(models.Model):
  play = models.ForeignKey(Play)
#  user = models.ForeignKey(User)
  award_points = models.IntegerField()
