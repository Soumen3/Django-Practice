from django.urls import path 
from . import views 

urlpatterns = [
    path('signup/',views.signUp, name='signup'),
    path('login/', views.UserLogin, name='login'),
    path('dashboard/', views.dashboard,  name='dashboard'),
    path('logout/',views.UserLogout,name='logout'),
]
