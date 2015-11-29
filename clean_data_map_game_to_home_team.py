import csv

f = open('cfl_games.csv', 'rt')
reader = csv.reader(f)

o = open('cleaned_map_game_to_home_team.csv', 'w')

for row in reader:
  o.write("%s,%s\n" % (row[1], row[19]))
