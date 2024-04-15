from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.


def setcookie(request):
    response = render(request, 'setcookie.html')
    # response.set_cookie('name', 'Soumen', max_age=60)
    response.set_signed_cookie('name', 'Soumen', salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    # name=request.COOKIES['name']
    name= request.get_signed_cookie('name', salt='nm')       # same as above, it will return a None value id no cookie is available | salt will be same as the setcookie
    return render(request, 'getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response