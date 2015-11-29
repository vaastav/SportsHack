import pandas as pd
import numpy as np
import csv

def main():
  team_data = pd.read_csv('team_data.csv')
  fieldnames = ['name','wins','loss','points','points_scored','points_conceded']
  outf = open('team_model_data.csv','w')
  writer = csv.DictWriter(outf,delimiter=',',lineterminator='\n',fieldnames=fieldnames)
  writer.writeheader()
  for team in np.unique(team_data.name):
    spec_data = team_data[team_data.name == team]
    row = {}
    row['name'] = team
    row['wins'] = np.sum(spec_data.win)
    row['loss'] = np.sum(spec_data.loss)
    row['points'] = np.sum(spec_data.points)
    row['points_scored'] = np.sum(spec_data.points_scored)
    row['points_conceded'] = np.sum(spec_data.points_conceded)
    writer.writerow(row)


if __name__ == '__main__':
  main()