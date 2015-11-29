from django.shortcuts import render
from predictor.models import User
from predictor.models import Game

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
  context = {'games': games}
  return render(request, 'predictor/game_select.html', games)
def leaderboard(request):
  context = { 'users': User.objects.all().order_by('points') }
  return render(request, 'predictor/leaderboard.html', context) 

