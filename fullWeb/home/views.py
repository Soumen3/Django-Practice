from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
# Create your views here.

# def home_page(request):
#     return HttpResponse(
#         '<h1> search python and django</h1>'
#     )

def home_page(request):
    cntxt={
        'date':datetime.now(),
        'courses':['python','django','html','css','javascript','react','bootstrap','Nodejs'],
    }
    return render(request,'home/homePage.html',context=cntxt)