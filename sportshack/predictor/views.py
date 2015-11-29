from django.shortcuts import render
from predictor.models import User
from predictor.models import Game

import predictor.play_classifier as pc
import datetime
import csv

def get_plays(game_id):
  f = open('predictor/cleaned_map_state_to_play_v2.csv', 'rt')
  reader = csv.reader(f)
  times = []
  states = []
  results = []
  for row in reader:
    if row[0] == game_id:
      times.append( int(row[1]) * 15 + 900 - int(row[2]) )
      states.append( row[1:-1] )
      results.append( row[-1] )
  return (times, states, results)
    

# Create your views here.
def index(request):
  return render(request, 'predictor/index.html')
def home(request):
  pc.train()  

  #call train method from here  
  game = request.GET.get('game')
  time = request.GET.get('time')
  game_id = request.GET.get('game_id')

  times, states, res = get_plays(game_id)
  probs = [ pc.predict_probabilities( [int(i) for i in state] ) for state in states ]

  return render(request, 'predictor/home.html', {'game_id': game_id, 'game': game, 'time': time, 'times': times, 'states': states, 'res': res, 'probs': probs})
def login(request):
  return render(request, 'predictor/login.html')
def signup(request):
  return render(request, 'predictor/signup.html')

def select(request):
  games = Game.objects.all()
  today = datetime.date.today()
  games = [ i for i in games if i.date.day == 14 and i.date.month == 9 and i.date.year == 2013]
  context = {'games': games}


  return render(request, 'predictor/game_select.html', context)



def leaderboard(request):
  context = { 'users': User.objects.all().order_by('points') }
  return render(request, 'predictor/leaderboard.html', context) 

