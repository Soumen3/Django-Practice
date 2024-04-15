from django.shortcuts import render

# Create your views here.
def pyhtonPage(request):
    cntxt={
        'name':'coder camp',
        'fees':5000,
        'courseName':'python',
    }
    return render(request, 'python/pythonPage.html', context=cntxt)