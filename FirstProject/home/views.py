from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return  HttpResponse(
        "<center>Program run successfully</center>"
    )