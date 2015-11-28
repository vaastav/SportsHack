import pandas as pd
import numpy as np
import csv

def calc_aggression(row):
  return ((1.12*row['average_attempted_passes']*row['average_pass_completion'] + average_yards_per_completed_pass + average_yards_per_attempted_pass + average_yards_per_rush/average_yards_per_play/50))

def main():
  team_data = pd.read_csv('cleaned_team_stats.csv')
  with open('team_aggression_factor.csv','w') as outf:
    fieldnames = ['team_name','num_games','average_yards_per_play','average_pass_completion','average_attempted_passes','average_yards_per_rush','average_yards_per_completed_pass','average_yards_per_attempted_pass','aggression']
    writer = csv.DictWriter(outf,delimiter=',',lineterminator='\n',fieldnames=fieldnames)
    writer.writeheader()

    for team in np.unique(team_data.team_name):
      team_specific_data = team_data[team_data.team_name == team]
      row = {}
      row['team_name'] = team
      row['num_games'] = len(team_specific_data)
      row['average_yards_per_play'] = np.average(team_specific_data.yards_per_play)
      row['average_pass_completion'] = np.average(team_specific_data.pass_completion)
      row['average_yards_per_rush'] = np.average(team_specific_data.yards_per_rush)
      row['average_yards_per_attempted_pass'] = np.average(team_specific_data.yards_per_attempted_pass)
      row['average_yards_per_completed_pass'] = np.average(team_specific_data.yards_per_completed_pass)
      row['average_attempted_passes'] = np.average(team_specific_data.attempted_passes)
      row['aggression'] = calc_aggression(row)
      writer.writerow(row)
      
if __name__ == '__main__':
  main()
