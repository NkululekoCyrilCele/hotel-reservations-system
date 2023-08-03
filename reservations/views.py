from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from .models import Room, Guest


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
    available_rooms = Room.objects.filter(is_available=True)
    return render(request, "available_rooms.html", {"available_rooms": available_rooms})


def guest_details(request):
    guests = Guest.objects.all()
    return render(request, "guest_details.html", {"guests": guests})
