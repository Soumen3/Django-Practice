from django.shortcuts import render


def setsession (request):
    request.session['name']='Sonam'
    request.session.set_expiry(600)
    return render(request, 'setsession.html')

def getsession(request):
    name=request.session['name']

    return render(request, 'getsession.html', {'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')
