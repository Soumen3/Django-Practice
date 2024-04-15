from django.shortcuts import render
from .forms import signUpForm
from django.contrib import messages

# Create your views here.
def signUp(request):
    context={}
    if request.method=='POST':
        fm=signUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account has been created successfully')
            fm.save()
    else:
        fm=signUpForm()
    context['form']=fm
    return render(request, 'signup.html', context)
    
