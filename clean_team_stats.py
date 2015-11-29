import csv

def calc_points_scored(row):
  if row['loc'] == 'H':
    return row['home_score']
  else:
    return row['away_score']

def calc_points_conceded(row):
  if row['loc'] == 'H':
    return row['away_score']
  else:
    return row['home_score']

def calc_res(a,b):
  return a > b

def main():
  with open('cfl_team_stats.csv','r') as inf:
    reader = csv.DictReader(inf)
    with open('cleaned_team_stats.csv','w') as outf:
      fieldnames = ['team_id','team_name','yards_per_play','pass_completion','yards_per_rush','yards_per_attempted_pass','yards_per_completed_pass','attempted_passes']
      writer = csv.DictWriter(outf, delimiter=',',lineterminator='\n',fieldnames=fieldnames)
      fieldnames2 = ['name','win','loss','points','points_scored','points_conceded']
      outf2 = open('team_data.csv','w')
      writer2 = csv.DictWriter(outf2,delimiter=',',lineterminator='\n',fieldnames=fieldnames2)
      writer2.writeheader()
      writer.writeheader()
      for row in reader:
	      writer.writerow({'team_id':row['team_id'],'team_name':str(row['city']) + ' ' + str(row['team_name']),'yards_per_play':row['game_totals_average'],'pass_completion':float(row['passing_completions'])/float(row['passing_attempts']),'yards_per_rush':row['rushing_average'],'yards_per_attempted_pass':row['passing_average'],'yards_per_completed_pass':float(row['passing_yards'])/float(row['passing_completions']),'attempted_passes':row['passing_attempts']})
	      new_row = {}
	      new_row['name'] = str(row['city']) + ' ' + str(row['team_name'])
	      new_row['points'] = 0
	      new_row['points_scored'] = calc_points_scored(row)
	      new_row['points_conceded'] = calc_points_conceded(row)
	      new_row['win'] = calc_res(new_row['points_scored'],new_row['points_conceded'])
	      new_row['loss'] = calc_res(new_row['points_conceded'],new_row['points_scored'])
	      writer2.writerow(new_row)

if __name__ == '__main__':
  main()
