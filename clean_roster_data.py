import csv

f = open('cfl_roster.csv', 'rt')
reader = csv.reader(f)

o = open('cleaned_roster1.csv', 'w')

for row in reader:
	print(row[1])
	#o.write("%s,%s,%s,%s,%s,\n" % (row[0],row[4],row[5],row[11], row[12]))