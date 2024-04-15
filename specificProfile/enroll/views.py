from django.shortcuts import render, redirect
from .forms import signUpForm, profileUpdateForm, AdminProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
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
    context={}
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser == True:
                fm=AdminProfileUpdateForm(request.POST, instance=request.user)
            else:
                fm=profileUpdateForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Data updated')
            else:
                messages.error(request, 'Invalid input')
                
        else:
            if request.user.is_superuser == True:
                fm= AdminProfileUpdateForm(instance=request.user)
                TotalUser=User.objects.all()
            else:
                fm=profileUpdateForm(instance=request.user)
                TotalUser=None

        context['form']=fm
        context['name']=request.user.first_name
        context['users']=TotalUser
        return render(request, 'profile.html', context)
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




def user_detail(request,id):
    if request.user.is_authenticated:
        PiKey=User.objects.get(pk=id)
        fm=AdminProfileUpdateForm(instance=PiKey)
        
        return render(request, 'userdetail.html', {'form':fm})
    else:
        return redirect('login')