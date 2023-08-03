from .forms import ReservationForm
from .models import Reservation

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from .models import Room, Guest, Reservation, Contact
from .forms import GuestForm, ReservationForm, ContactForm


def index(request):
    return render(request, "index.html")


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


def assign_room(request, guest_id):
    guest = get_object_or_404(Guest, id=guest_id)

    if request.POST == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            selected_room_id = form.cleaned_data["room"]
            selected_room = get_object_or_404(Room, id=selected_room_id)
            reservation = Reservation.objects.create(
                guest=guest, room=selected_room, check_in_date=form.cleaned_data["check_in_date"], check_out_date=form.cleaned_data["check_out_date"])
            return redirect("guest_details")
    else:
        form = ReservationForm()
    return render(request, "assign_room.html", {"form": form, "guest": guest})


def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect("reservation_success")
    else:
        form = ReservationForm()

    return render(request, "make_reservation.html", {"form": form})


def reservation_success(request):
    return render(request, "reservation_success.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"]
            )
            return redirect("thank_you")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def thank_you(request):
    return render(request, "thank_you.html")
