from django.shortcuts import render
from . import forms
from .models import User
# Create your views here.


def showForm(request):
    if request.method == 'POST':
        fm = forms.Formdata(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            userObj = User(name=nm, email=em, password=ps)
            userObj.save()
            return render(request, 'enroll/save.html')

    else:
        fm=forms.Formdata()
    return render(request, 'enroll/page.html', {'form':fm})
