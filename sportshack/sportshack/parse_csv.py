from predictor.models import Game,Team
import csv

def read_game_file(csvfile):
  reader = csv.DictReader(csvfile)
  for row in reader:
    Game.objects.create( home_team = row['home_team'],away_team = row['away_team'],home_score=int(row['home_score']),away_score = int(row['away_score']),home_qt1=int(row['home_qt1']),home_qt2 = int(row['home_qt2']), home_qt3 = int(row['home_qt3']), home_qt4 = int(row['home_qt4']), away_qt1 = int(row['away_qt1']), away_qt2 = int(row['away_qt2']), away_qt3 = int(row['away_qt3']),away_qt4 = int(row['away_qt4'])


def read_team_file(csvfile):
  reader = csv.DictReader(csvfile)
  for row in reader:
    Team.objects.create( name = row['name'],win = row['wins'],loss=row['loss'],points=row['points'],points_scored=row['points_scored'],points_conceded=row['points_conceded'])
    
