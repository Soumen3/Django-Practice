from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.

# create cache using .get() and .set()
# def home(request):
#     mv=cache.get('movie', 'has_expired')
#     if mv== 'has_expired':
#         cache.set('movie', 'the one', 20)     # the cache will store for 20 seconds
#         mv= cache.get('movie')

#     return render(request, 'course.html',{'fm':mv})


# create cache using .get_or_set()
# def home(request):
#     mv= cache.get_or_set('fees', 45000, 20)       # the cache will store for 20 seconds
#     return render(request, 'course.html',{'fm':mv})



# create cache using .set_many() .get_many()
# def home(request):
#     data={'name':'Soumen manta', 'roll':1}
#     cache.set_many(data, 30)        # the cache will store for 30 seconds
#     mv=cache.get_many(data)
#     return render(request, 'course.html',{'fm':mv})



# delete cache 
# def home(request):
#     cache.delete('roll')
#     return render(request, 'course.html')




# clear cache 
def home(request):
    cache.clear()
    return render(request,'course.html')
