from django.urls import path 
from . import views
urlpatterns = [
    path('',views.show_home, name='home'),
    path('stu/<my_id>/', views.show_details, name='details'),
    path('stu/<my_id>/<int:my_subid>/', views.show_details, name='details')
]
