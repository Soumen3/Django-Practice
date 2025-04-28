from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_or_update/", views.create_or_update_model, name="create_or_update"),
    path("mymodel_form/", views.mymodel_form_view, name="mymodel_form"),
]