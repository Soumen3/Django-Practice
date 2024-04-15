from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.

def formPage(request):
    
    if request.method=='POST':

        fm=forms.studentRegistration(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['Roll'])
            print(fm.cleaned_data['Price'])
            print(fm.cleaned_data['Rate'])
            print(fm.cleaned_data['agree'])
            return redirect('success')
    else:
        fm=forms.studentRegistration()
    return render(request, 'enroll/page.html',{'form':fm})

def succPage(request):
    return render(request, 'enroll/success.html')