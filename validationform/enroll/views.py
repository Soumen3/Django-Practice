from django.shortcuts import render,redirect
from .forms import studentRegistration

# Create your views here.
def registration(request):

    if request.method=='POST':
        fm=studentRegistration(request.POST)
        # return redirect('success')
        
    else:
        fm=studentRegistration()

    return render(request, 'enroll/page.html', context={'form':fm})


def success(request):
    return render (request, 'enroll/success.html')