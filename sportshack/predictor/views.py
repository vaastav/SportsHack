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

