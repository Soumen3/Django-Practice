from django.shortcuts import render


def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'settestcookie.html')


def checktestcookie(request):
    value=request.session.test_cookie_worked()
    return render(request, 'checktestcookie.html', {'value':value})


def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'deltestcookie.html')

