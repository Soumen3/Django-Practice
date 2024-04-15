from django.urls import path
from . import views

urlpatterns=[
    path('djangofees/',views.fees_django),
    path('pythonfees/',views.fees_python),
]