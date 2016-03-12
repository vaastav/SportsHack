import csv

def main():
  with open('cfl_team_stats.csv','r') as inf:
    reader = csv.DictReader(inf)
    with open('cleaned_team_defense_stats.csv','w') as outf:
      fieldnames = ['team_id','team_name','interception_returns_attempts','interception_returns_yards','defense_tackles','defense_sacks','defense_sack_yards','defense_passes_defensed','defense_forced_fumbles','defense_fumble_recoveries','special_teams_tackles']
      writer = csv.DictWriter(outf,delimiter=',',lineterminator='\n',fieldnames=fieldnames)
      writer.writeheader()
      for row in reader:
        writer.writerow({'team_id':row['team_id'],'team_name':str(row['city']) + ' ' + str(row['team_name']),'interception_returns_attempts':row['interception_returns_attempts'],'interception_returns_yards':row['interception_returns_yards'],'defense_tackles':row['defense_tackles'],'defense_sacks':row['defense_sacks'],'defense_sack_yards':row['defense_sack_yards'],'defense_passes_defensed':row['defense_passes_defensed'],'defense_forced_fumbles':row['defense_forced_fumbles'],'defense_fumble_recoveries':row['defense_fumble_recoveries'],'special_teams_tackles':row['special_teams_tackles']})

if __name__ == '__main__':
  main()
