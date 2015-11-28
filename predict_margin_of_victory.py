# based on the current elo data for two teams. predict the margin of victory between them
import csv

f = open('cleaned_game_tbl.csv', 'rt')
reader = csv.reader(f)

elos = {}

def predict_margin_of_victory(team_a, team_b):
  if elos[team_a] > elos[team_b]:
    return "%s Victory! Point difference will be %s" % (team_a, (elos[team_a] - elos[team_b])/25)
  else:
    return "%s Victory! Point difference will be %s" % (team_b, (elos[team_b] - elos[team_a])/25)

for row in reader:
  elos[row[1]] = float(row[2])

while True:
  team_a = input("Name of team A (eg. BC/Edmonton/Ottawa): ")
  team_b = input("Name of team B (eg. BC/Edmonton/Ottawa): ")
  print(predict_margin_of_victory(team_a, team_b))

