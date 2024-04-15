from django.urls import path 
from enroll import views

urlpatterns = [
    path('',views.formPage,),
    path('success/',views.succPage, name='success')
]
