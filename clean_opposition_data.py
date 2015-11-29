import csv

f = open('cfl_team_stats.csv', 'rt')
reader = csv.reader(f)

o = open('cleaned_team_opposition.csv', 'w')

tempVar = "";
for row in reader:
	if(row[92] == 'H'):
		o.write("%s,%s,\n" % (row[2]+" "+row[3], row[70]))