from django.shortcuts import render
from .forms import Registration
# Create your views here.

def ShowPaage(request):

    if request.method=='POST':
        fm=Registration(request.POST)
    else:
        fm=Registration()
    return render (request, 'enroll/page.html', {'form':fm})