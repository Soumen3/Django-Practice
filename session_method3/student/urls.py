from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.checktestcookie, name='set'),
    path('set/', views.settestcookie, name='get'),
    path('del/', views.deltestcookie, name='del'),
]
