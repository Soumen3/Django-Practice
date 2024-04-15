from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_text(request):
    return HttpResponse('<h1>Hello Everyone <br>This is my first project</h1>')

def learn_django(request):
    return HttpResponse('<h2>Thos is django</h1>')

def learn_math(request):
    return HttpResponse(10+20)

def learn_python(request):
    a='<h2>This is python</h1>'
    return HttpResponse(a)

def learn_format(request):
    a="Soumen"
    return HttpResponse(f'hello {a}')

def home(request):
    return HttpResponse("<h1>This is the home page</h1>")