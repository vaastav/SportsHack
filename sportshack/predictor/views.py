from django.shortcuts import render

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
	return render(request, 'predictor/game_select.html')
def leaderboard(request):
	return render(request, 'predictor/leaderboard.html')

