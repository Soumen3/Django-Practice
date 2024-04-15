from django.shortcuts import render, redirect
from .forms import signUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
# Create your views here.

def signUp(request):
    if request.method=='POST':
        fm=signUpForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='Editor')
            user.groups.add(group)
            messages.success(request,'Account has been created')
        else:
            messages.error(request,'Invalid Inputs')

    else:
        fm=signUpForm()
    return render(request,'signup.html', {'form':fm})

def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm= AuthenticationForm(request=request ,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data['username']
                password=fm.cleaned_data['password']

                user= authenticate(username=username, password=password)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfull')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'User dose not exist')
            else:
                messages.error(request,'Invalid data')
        
        else:
            fm=AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
        return redirect('dashboard')





def dashboard(request):
    
    if request.user.is_authenticated:
        return render(request, 'dashboard.html',{"name":request.user})
    else:
        return redirect('login')
    



def UserLogout(request):
    logout(request)
    return redirect('login')


