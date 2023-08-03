from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("register/", views.register, name="register"),
    path("login/", views.custom_login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("available_rooms/", views.available_rooms, name="available_rooms"),
    path("guest_details/", views.guest_details, name="guest_details"),
    path("reservation_details/", views.reservation_details,
         name="reservation_details"),
    path("edit_guest/<int:guest_id>/", views.edit_guest, name="edit_guest"),
    path("assign_room/<int:guest_id>/", views.assign_room, name="assign_room"),
    path("make_reservation/", views.make_reservation, name="make_reservation"),
    path("reservation_success/", views.reservation_success,
         name="reservation_success"),
    path("thank_you/", views.thank_you, name="thank_you"),
]
