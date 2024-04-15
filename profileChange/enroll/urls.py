from django.urls import path 
from . import views 

urlpatterns = [
    path('signup/',views.signUp, name='signup'),
    path('login/', views.UserLogin, name='login'),
    path('profile/', views.profile,  name='profile'),
    path('logout/',views.UserLogout,name='logout'),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('changepass2/',views.user_change_pass2,name='changepass2'),
    
]
