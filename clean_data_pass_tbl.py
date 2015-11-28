import csv

f = open('cfl_play_by_play.csv', 'rt')
reader = csv.reader(f)

o = open('cleaned_pass_tbl.csv', 'w')

for row in reader:
  # if play_type_id is 1 (pass) store game_id, play_id, passer, receiver, tackler
  if row[14].isdigit() and int(row[14]) == 1:
    o.write("%s,%s,%s,%s,%s\n" % (row[0], row[1], row[15], row[16], row[18]))
