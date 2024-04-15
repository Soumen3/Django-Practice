from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.registration),
    path('success/',views.success, name='success')
]
