from django.urls import path 
from . import views
urlpatterns = [
    path('signup/',views.signUp, name='signup'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.User_logout,name='logout'),
]
