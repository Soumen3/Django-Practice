from . import views
from django.urls import path

urlpatterns = [
    path('python/',views.pyhtonPage, name='pythonPage'),
]
