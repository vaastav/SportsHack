import pandas as pd
import numpy as np
import csv

def main():
  play_by_play_data = pd.read_csv('cfl_play_by_play.csv')
  rush_data = play_by_play_data[ play_by_play_data.id == 4 ]
  with open('cleaned_rush_table.csv','w') as outf:
    fieldnames = ['game_id','play_id','player1_id','tackle1_id']
    writer = csv.DictWriter( outf, fieldnames = fieldnames)
    writer.writeheader()
    
    for row in rush_data.iterrows():
      writer.writerow({'game_id':row[0],'play_id':row[1][0],'player1_id':row[1][15],'tackle1_id':row[1][18]})
      

if __name__ == '__main__':
  main()
