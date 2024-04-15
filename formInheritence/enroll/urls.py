from django.urls import path 
from . import views

urlpatterns = [
    path('stu',views.student_form, name='Student' ),
    path('teach',views.teacher_form, name='Teacher' ),
]
