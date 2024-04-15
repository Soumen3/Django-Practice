from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.ShowPaage, name='page'),
]
