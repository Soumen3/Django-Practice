from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
'''def learn_django(request):
    return HttpResponse(
        '<h1>hello django</h1>'
    )

def learn_python(request):
    return HttpResponse(
        '<h1>hello python</h1>'
    )
'''

def learn_django(request):
    cntxt={                         # Dynamic type data
        'year':2023,
        'name':'django',
        'seat':40,
        'duration':'4 months',
        'date':datetime.now(),
        'age':18,
    }
    return render(request,'course/django.html', context=cntxt)

def learn_python(request):
    cntxt={                         # Dynamic type data
        'year':2023,
        'name':'python',
        'seat':30,
        'duration':'6 months',
        'date':datetime.now(),
        'age':18,
    }
    return render(request,'course/python.html', context=cntxt)