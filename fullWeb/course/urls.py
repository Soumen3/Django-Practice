from django.urls import path
from . import views

urlpatterns=[
    path('django/',views.learn_django),
    path('python/',views.learn_python),
]