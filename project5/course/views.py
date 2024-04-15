from django.shortcuts import render

# Create your views here.
def homePage(request):
    cntxt={
        'name':'coder camp',
        'courses':['python','django', 'html', 'css','js', 'tailwind', 'bootstrap', 'c', 'c++', 'c#', 'java', 'dsa',],
        'seats':50,
        'start':'01.05.2023',
    }

    return render(request, "course/home.html", context=cntxt)