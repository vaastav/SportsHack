from sklearn import svm
import csv

f = open('cleaned_map_state_to_play_v2.csv', 'rt')
reader = csv.reader(f)

X = []
Y = []

for row in reader:
  nrow = [ int(i) for i in row[:-1] ]
  X.append(nrow)
  Y.append(int(row[-1]))

# 1 v 1 (create n*(n-1)/2 models)
clf = svm.SVC(decision_function_shape='ovo')

# 1 v r (create n models)
#lin_clf = svm.LinearSVC()
clf.fit(X,Y)


print("prediction ready")

while True:
  in_arr = [int(i) for i in input().split(",")]
  print("input_received")
  print(clf.predict([in_arr]))
  print(clf._predict_proba_lr([in_arr]))
