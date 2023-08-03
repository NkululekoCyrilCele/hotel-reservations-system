from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.custom_login, name="login"),
    path("available_rooms/", views.available_rooms, name="available_rooms"),
]
