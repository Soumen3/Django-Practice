from django.urls import path
from . import views

urlpatterns=[
    path('pythonFees/',views.pythonFees),
    path('djangoFees/',views.djangoFees),
]