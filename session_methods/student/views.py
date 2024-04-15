from django.shortcuts import render


def setsession (request):
    request.session['name']='Sonam'
    return render(request, 'setsession.html')

def getsession(request):
    keys= request.session.keys()
    values= request.session.values()
    items=request.session.items()
    age= request.session.setdefault('age', 21)                  # return the value if exists, otherwise set the given defalut value and return
    return render(request, 'getsession.html', {'keys':keys, 'values':values, 'items':items, 'age':age})

def delsession(request):
    request.session.flush()
    return render(request, 'delsession.html')
