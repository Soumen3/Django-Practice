from django.shortcuts import render, redirect
from .forms import signUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def signUp(request):
    context = {}
    if request.method == 'POST':
        fm = signUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Data Uploded successfully')
        else:
            messages.error(
                request, 'Something wrong. Contact to the developer')
    else:
        fm = signUpForm()
    context['form'] = fm
    return render(request, 'signup.html', context)


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfull')
                    return redirect('profile')
                else:
                    messages.error(request,'Something wrong')
            else:
                messages.error(request,'Data is inavalid')
        else:
            fm = AuthenticationForm()
        return render(request, 'userLogin.html', {'form': fm})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name':request.user})
    else:
        return redirect('login')


def User_logout(request):
    logout(request)
    return redirect ('login')