import csv

f = open('cfl_games.csv', 'rt')
reader = csv.reader(f)

o = open('cleaned_game_tbl.csv', 'w')

elos = {}
reset = False

for i,row in enumerate(reader):
  if not i:
    continue

  game_date = row[6]

  if reset:
    reset = not reset
    for k in elos.keys():
      elos[k] = 0.75*elos[k] + 0.25*1505
      o.write("%s,%s,%s\n" % (game_date, home_team, elos[home_team]))
      o.write("%s,%s,%s\n" % (game_date, away_team, elos[away_team]))


  home_team = row[18]
  home_score = sum(int(i) if i != 'NULL' else 0 for i in row[20:25])
  away_team = row[10]
  away_score = sum(int(i) if i != 'NULL' else 0 for i in row[12:17])

  if home_team not in elos:
    elos[home_team] = 1500
  if away_team not in elos:
    elos[away_team] = 1500

  if home_score > away_score:
    mov = home_score - away_score
    delo = 25*((mov + 3) ** 0.8)/(7.5 + 0.006 * (elos[home_team] - elos[away_team]))
    elos[home_team] += delo
    elos[away_team] -= delo
  else:
    mov = away_score - home_score
    delo = 25*((mov + 3) ** 0.8)/(7.5 + 0.006 * (elos[away_team] - elos[home_team]))
    elos[away_team] += delo
    elos[home_team] -= delo

  o.write("%s,%s,%s\n" % (game_date, home_team, elos[home_team]))
  o.write("%s,%s,%s\n" % (game_date, away_team, elos[away_team]))

  if row[3] == 'GC':
    reset = True
  
  
