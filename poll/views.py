from django.shortcuts import render
import datetime


def home(request):
	time = datetime.datetime.now()

	context = { 
	'timeanddate' : time
	}
	return render(request, 'poll/home.html', context)