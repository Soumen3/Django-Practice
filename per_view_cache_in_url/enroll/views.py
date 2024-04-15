from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(20) # Cache for 20 second
def home(request):
    return render(request, 'course.html')


def contact(request):
    return render(request, 'contact.html')