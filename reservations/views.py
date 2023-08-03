from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from .models import Room, Guest, Reservation
from .forms import GuestForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def custom_login(request):
    return LoginView.as_view(template_name="registration/login.html")(request)


def available_rooms(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, "available_rooms.html", {"rooms": rooms})


def guest_details(request):
    guests = Guest.objects.all()
    return render(request, "guest_details.html", {"guests": guests})


def reservation_details(request):
    reservations = Reservation.objects.all()
    return render(request, "reservation_details.html", {"reservations": reservations})


def edit_guest(request, guest_id):
    guest = get_object_or_404(Guest, id=guest_id)

    if request.method == "POST":
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect("guest_details")
    else:
        form = GuestForm(instance=guest)
    return render(request, "edit_guest.html", {"form": form})
