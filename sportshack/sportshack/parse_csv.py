from predictor.models import Game,Team,Player
from django.http import HttpResponse
import csv

def read_game_file(csvfile):
  reader = csv.DictReader(csvfile)
  for row in reader:
    Game.objects.create( home_team = row['home_team'],away_team = row['away_team'],home_score=int(row['home_score']),away_score = int(row['away_score']),home_qt1=int(row['home_qt1']),home_qt2 = int(row['home_qt2']), home_qt3 = int(row['home_qt3']), home_qt4 = int(row['home_qt4']), away_qt1 = int(row['away_qt1']), away_qt2 = int(row['away_qt2']), away_qt3 = int(row['away_qt3']),away_qt4 = int(row['away_qt4']),date=row['date'])

def read_team_file(csvfile):
  reader = csv.DictReader(csvfile)
  for row in reader:
    Team.objects.create( name = row['name'],win = row['wins'],loss=row['loss'],points=row['points'],points_scored=row['points_scored'],points_conceded=row['points_conceded'])

def read_player_file(csvfile):
  reader = csv.DictReader(csvfile)
  for row in reader:
    try:
      Player.objects.create(first_name = row['first'],last_name=row['last'],touchdown=int(row['touchdowns']),points=int(row['points']),fumbles=int(row['fumbles']),height=float(row['height']),weight=int(row['weight']),birthplace=row['birthplace'],position=row['position'],team=row['team'])
    except:
      continue

def flush_data(request):
  Game.objects.all().delete()
  Team.objects.all().delete()
  Player.objects.all().delete()
  return HttpResponse('Success!')

def import_data(request):
  read_game_file(open('predictor/data/game_data.csv','r'))
  read_team_file(open('predictor/data/team_model_data.csv','r'))
  read_player_file(open('predictor/data/players_clean.csv','r'))
  return HttpResponse('Success!')
