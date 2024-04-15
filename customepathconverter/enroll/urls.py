from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYear, 'yyyy')
urlpatterns = [
    path('', views.home_page, name='home' ),
    path('batch/<yyyy:year>', views.batches, name='details')
    
]
