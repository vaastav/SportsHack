import pandas as pd
import numpy as np
import csv

def main():
  play_by_play_data = pd.read_csv('cfl_play_by_play.csv')
  type_id = play_by_play_data.id
  id_enum = {}
  for ide in np.unique(type_id):
    id_enum[ide] = np.unique(play_by_play_data[type_id == ide].name)[0]
    print(ide,id_enum[ide])

  id_enum[0] = 'Touchdown'

  with open('enumerations.csv','w') as outf:
    fieldnames = ['Type_Id','Type_Name']
    writer = csv.DictWriter(outf, fieldnames = fieldnames)

    writer.writeheader()
    for ide,name in id_enum.items():
      writer.writerow({'Type_Id':ide, 'Type_Name':name})

if __name__ == '__main__':
  main()
