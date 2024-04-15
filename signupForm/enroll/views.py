from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signUp(request):
    context={}
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=UserCreationForm()
    context['form']=fm
    return render(request, 'signup.html', context)