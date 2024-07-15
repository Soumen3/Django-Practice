from django.shortcuts import render, HttpResponse
from . import signals

# Create your views here.
def home(request):
	signals.notification.send(sender=None, request=request, user=["User1", "User2"])
	return HttpResponse("This is Home Page")