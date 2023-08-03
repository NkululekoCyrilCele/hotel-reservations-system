from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.custom_login, name="login"),
    path("available_rooms/", views.available_rooms, name="available_rooms"),
    path("guest_details/", views.guest_details, name="guest_details"),
    path("reservation_details/", views.reservation_details,
         name="reservation_details"),
    path("edit_guest/<int:guest_id>/", views.edit_guest, name="edit_guest"),
    path("assign_room/<int:guest_id>/", views.assign_room, name="assign_room"),
]
