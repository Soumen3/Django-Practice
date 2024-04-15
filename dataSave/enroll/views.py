from django.shortcuts import render
from .forms import UserDetails
from .models import User
# Create your views here.


def homePage(request):
    if request.method == 'POST':
        fm = UserDetails(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']

            userObj = User(id=1, name=nm,  email=em, password=ps)
            # userObj.name=nm
            # userObj.email=em                  it is also works
            # userObj.password=ps
            userObj.save()

    else:
        fm = UserDetails()
    return render(request, 'enroll/page.html', {'form': fm})
