from django.shortcuts import render


def setsession (request):
    request.session['name']='Sonam'
    request.session['lname']='Jha'
    return render(request, 'setsession.html')

def getsession(request):
    # name=request.session['name']                              # You can't set adefault value in this, the will through an error if key doesn't  match
    name=request.session.get('name', default='Guest')           # same as above, only you can set a default value, so key error will not appear
    lname=request.session.get('lname', default='Guest')
    return render(request, 'getsession.html', {'name':name, 'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    
    return render(request, 'delsession.html')
