from django.shortcuts import render

# Create your views here.
def djangoPage(request):
    cntxt={
        'courseName':'django',
        'seats': 45,
        'start': '01.05.2023'
    }
    return render(request, 'djangoApp\djangoPage.html', context=cntxt)