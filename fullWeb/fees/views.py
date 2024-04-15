from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''def fees_django(request):
    return HttpResponse(
        '<h1>django-3000</h1>'
    )

def fees_python(request):
    return HttpResponse(
        '<h1>python-4000</h1>'
    )'''

def fees_django(request):
    return render(request,'fees/djangofees.html')

def fees_python(request):
    return render(request,'fees/pythonfees.html')