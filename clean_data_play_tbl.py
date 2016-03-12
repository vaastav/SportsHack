import csv

f = open('cfl_play_by_play.csv', 'rt')
reader = csv.reader(f)

o = open('cleaned_play_tbl.csv', 'w')

for row in reader:
  # game_id, play_id, quarter, time, down, distance, away_score_before, away_score_after, home_score_before, home_score_after, yardline, end_yardline, end_possession_id, continuation,  play_type_id, details, result_id, result_name
  o.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[-3], row[-2], row[-1]))


  
