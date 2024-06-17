from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	print("I am View")
	return HttpResponse("This is Home Page")

def about(request):
	# print(request)
	print("I am about View")
	return HttpResponse("This is About Page")