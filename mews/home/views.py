from django.shortcuts import render


def index(request):
	return render(request, 'home/index.html')

def results(request):
	return render(request, 'home/results.html')