from django.http import HttpResponse
from django.shortcuts import render

from app.models import Event

def index(request):

	events = Event.objects.all()
	
	return render(
    	request,
    	'index.html',
    	{'events': events})
