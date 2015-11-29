from django.shortcuts import render
from predictor.models import User
from predictor.models import Game

import datetime

# Create your views here.
def index(request):
  return render(request, 'predictor/index.html')
def home(request):
  return render(request, 'predictor/home.html')
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

