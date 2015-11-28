from sklearn import svm, ensemble
import csv
from random import random

f = open('cleaned_map_state_to_play_v2.csv', 'rt')
reader = csv.reader(f)

X = []
Y = []

test_rows = []

for row in reader:
  if random() < 0.001 and len(test_rows) < 1000:
    test_rows.append( ( [int(i) for i in row[:-1]], int(row[-1]) ) )
    continue
  nrow = [ int(i) for i in row[:-1] ]
  X.append(nrow)
  Y.append(int(row[-1]))

# 1 v 1 (create n*(n-1)/2 models)
#clf = svm.SVC(decision_function_shape='ovo')

# 1 v r (create n models)
#lin_clf = svm.LinearSVC()
#lin_clf.fit(X,Y)


clf = ensemble.RandomForestClassifier(n_estimators=30, n_jobs=-1)
clf.fit(X,Y)

print("prediction ready")

sums = {}
counts = {}

for row in test_rows:
  print(row[0])
  print(row[1])
  if clf.predict([ row[0] ]) == row[1]:
    if row[1] in sums:
      sums[row[1]] += 1
      counts[row[1]] += 1
    else:
      sums[row[1]] = 1
      counts[row[1]] = 1
    print("SUCCESS")
  else:
    if row[1] in sums:
      sums[row[1]] += 0
      counts[row[1]] += 1
    else:
      sums[row[1]] = 0
      counts[row[1]] = 1
    print("FAILURE")
  
vsums = list(sums.values())
vcounts = list(counts.values())
print(sums.keys())
print(counts.keys())
print( [ vsums[i]/vcounts[i] for i in range(len(vsums)) ] )

while True:
  in_arr = [int(i) for i in input().split(",")]
  print("input_received")
  print(clf.predict([in_arr]))
  print(clf.predict_proba([in_arr]))
