from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# from .models import User

# Create your views here.
def registration(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'Your data has been saved.')
            messages.info(request, 'Now you can login')     # same as the above technique
    else:
        fm=StudentRegistration()
    return render(request, 'page.html', {'form':fm})