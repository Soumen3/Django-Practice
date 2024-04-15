from django.shortcuts import render
from datetime import datetime
# Create your views here.

def python_page(request):
    cntxt={
        'courses':['python', 'django', 'html', 'css', 'js', 'tailwind', 'bootstrap'],
        'seats':40,
        'price':5000,
        'date':datetime.now()
    }

    return render(request, 'main.html', context=cntxt)