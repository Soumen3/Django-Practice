from django.shortcuts import render

# Create your views here.
def pythonPG(request):
    cntxt={
        'courseName':'python',
        'seats': 45,
        'start': '01.05.2023'
    }

    return render(request, 'python/pythonPAGE.HTML', context=cntxt)