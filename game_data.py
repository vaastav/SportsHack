import csv

def main():
  teams = {}
  with open('team_ids.csv','r') as inf:
    reader = csv.DictReader(inf)
    for row in reader:
      teams[row['id']] = row['team']
  with open('cfl_team_stats.csv','r') as inf:
    reader = csv.DictReader(inf)
    with open('game_data.csv','w') as outf:
      fieldnames = ['game_id','home_team','away_team','home_score','away_score','home_qt1','home_qt2','home_qt3','home_qt4','away_qt1','away_qt2','away_qt3','away_qt4','date']
      writer = csv.DictWriter(outf,delimiter=',',lineterminator = '\n',fieldnames=fieldnames)
      writer.writeheader()
      for row in reader:
      	if row['loc'] == 'H':
          writer.writerow({'game_id': str(row['game_id']), 'home_team': str(row['city']) + ' ' + str(row['team_name']),'away_team':teams[row['away_team']],'home_score': row['home_score'],'away_score':row['away_score'], 'home_qt1':row['home_score1'], 'home_qt2':row['home_score2'],'home_qt3':row['home_score3'],'home_qt4':row['home_score4'],'away_qt1':row['away_score1'],'away_qt2':row['away_score2'],'away_qt3':row['away_score3'],'away_qt4':row['away_score4'],'date':row['game_date']})
if __name__ == '__main__':
  main()
