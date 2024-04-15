from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'enroll/home.html')

def batches(request, year):
    context={}
    context['yr']=year
    return render(request, 'enroll/pate.html', context)