from django.urls import path
from . import views


urlpatterns=[
    path("",views.home),
    path('learnTx/',views.learn_text),
    path('learnPy/',views.learn_python),
    path('learnDj/',views.learn_django),
    path('altlearnDj/',views.learn_django),
    path('learnM/',views.learn_math),
    path('learnF/',views.learn_format),
]