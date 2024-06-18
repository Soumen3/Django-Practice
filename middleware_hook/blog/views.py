from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
	print("I am View")
	return HttpResponse("This is Home Page")

def excep(request):
	print("I am exception View")
	a= 10/0
	return HttpResponse("This is exception view Page")

def user_info(request):
	print("I am User Info View")
	context={'name': 'Soumen', 'age': 22}
	return TemplateResponse(request, 'blog/user.html', context)
