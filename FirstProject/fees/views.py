from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def djangoFees(request):
    return HttpResponse(
        "<h3>For django Rs- 3000</h3> "
    )

def pythonFees(request):
    return HttpResponse(
        "<h3>For python Rs- 4000</h3> "
    )