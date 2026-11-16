from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("customer/add/", views.add_customer, name="add_customer"),
    path("medicine/add/", views.add_medicine, name="add_medicine"),
]
