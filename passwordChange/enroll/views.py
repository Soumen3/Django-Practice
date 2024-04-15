from django.shortcuts import render, redirect
from .forms import signUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def signUp(request):
    if request.method=='POST':
        fm=signUpForm(request.POST)
        if fm.is_valid():
            fm.save()
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
                    return redirect('profile')
                else:
                    messages.error(request, 'User dose not exist')
            else:
                messages.error(request,'Invalid data')
        
        else:
            fm=AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
        return redirect('profile')



def profile(request):
    if request.user.is_authenticated:
        # messages.warning(request,'Login Required')
        return render(request, 'profile.html', {'name': request.user})
    else:
        return redirect('login')
    
def UserLogout(request):
    logout(request)
    return redirect('login')


# change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)    # otherwise forcefully logout
                messages.success(request, 'Password changed')
                return redirect('profile')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render (request, 'changepass.html',  {'form':fm})
    else:
        return redirect('login')





# change password without old password
def user_change_pass2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)    # otherwise forcefully logout
                messages.success(request, 'Password changed')
                return redirect('profile')
        else:
            fm = SetPasswordForm(user=request.user)
        return render (request, 'changepass.html',  {'form':fm})
    else:
        return redirect('login')




