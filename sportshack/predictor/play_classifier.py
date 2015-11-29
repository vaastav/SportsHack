from sklearn import ensemble
import csv
from random import random

f = open('predictor/cleaned_map_state_to_play_v2.csv', 'rt')
reader = csv.reader(f)

X = []
Y = []

trained = False
def train():
  if trained:
    return True
  
  for row in reader:
    nrow = [ int(i) for i in row[1:-1] ]
    X.append(nrow)
    Y.append(int(row[-1]))

  clf = ensemble.RandomForestClassifier(n_estimators=100, n_jobs=-1)
  clf.fit(X,Y)
  trained = True

def predict_probabilities(in_arr):
  return clf.predict_proba([in_arr])

