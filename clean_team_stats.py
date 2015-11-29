import csv

def main():
  with open('cfl_team_stats.csv','r') as inf:
    reader = csv.DictReader(inf)
    with open('cleaned_team_stats.csv','w') as outf:
      fieldnames = ['team_id','team_name','yards_per_play','pass_completion','yards_per_rush','yards_per_attempted_pass','yards_per_completed_pass','attempted_passes']
      writer = csv.DictWriter(outf, delimiter=',',lineterminator='\n',fieldnames=fieldnames)
      writer.writeheader()
      for row in reader:
	      writer.writerow({'team_id':row['team_id'],'team_name':str(row['city']) + ' ' + str(row['team_name']),'yards_per_play':row['game_totals_average'],'pass_completion':float(row['passing_completions'])/float(row['passing_attempts']),'yards_per_rush':row['rushing_average'],'yards_per_attempted_pass':row['passing_average'],'yards_per_completed_pass':float(row['passing_yards'])/float(row['passing_completions']),'attempted_passes':row['passing_attempts']})

if __name__ == '__main__':
  main()
