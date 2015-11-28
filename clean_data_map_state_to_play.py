import csv

def parse_yardline(yardline):
  i = 0
  while not yardline[i].isdigit():
    i += 1
  return (yardline[:i], int(yardline[i:]))

f = open('cleaned_play_tbl.csv', 'rt')
reader = csv.reader(f)

g = open('cleaned_map_game_to_home_team.csv', 'rt')
greader = csv.reader(g)
g_hash = {}

for i, row in enumerate(greader):
  if i:
    g_hash[row[0]] = row[1]

o = open('cleaned_map_state_to_play.csv', 'w')

for i, row in enumerate(reader):
  if not i:
    continue

  #o.write("quarter,time,down,a_score,d_score,score_diff,yardline,yardline_dist,play_type_id)

  quarter, time, down = row[2:5]
  yardline, yardline_num = parse_yardline(row[10])
  attacking_team = yardline.lower()
  home = (int(row[4]) == 0) != (attacking_team == g_hash[row[0]])

  if home:
    a_score = int(row[8])
    d_score = int(row[6])
  else:
    a_score = int(row[6])
    d_score = int(row[8])

  dist_left = row[5]
  play_type_id = row[14]

  o.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (quarter, time, down, home, a_score, d_score, a_score - d_score, yardline_num, dist_left, play_type_id))
