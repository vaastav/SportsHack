import csv

f = open('cfl_roster_statsWorkingCopy.csv', 'rt')
reader = csv.reader(f)

o = open('newOutput2.csv', 'w')

tempFirstVal = 31;
touchDowncount = 0;
pointsCount = 0;
fumbleCount = 0;

for row in reader:

	if (row[0] == tempFirstVal):
		touchDowncount = touchDowncount + int(row[5])
		pointsCount = pointsCount + int(row[6])
		fumbleCount = fumbleCount + int(row[12])
	elif (row[0] != tempFirstVal):
		o.write("%s,%s,%s,%s,\n" % (str(tempFirstVal), str(touchDowncount), str(pointsCount), str(fumbleCount))) 
		tempFirstVal = row[0]
		touchDowncount = 0;
		pointsCount = 0;
		fumbleCount = 0;
