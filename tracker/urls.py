from django.urls import path
from . import views

urlpatterns = [
    path("sw.js", views.service_worker, name="service_worker"),
    path("", views.home, name="home"),
    path("customer/add/", views.add_customer, name="add_customer"),
    path("medicine/add/", views.add_medicine, name="add_medicine"),
    path("medicine/<int:pk>/delete/", views.delete_medicine, name="delete_medicine"),
]
