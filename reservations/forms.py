from django import forms
from .models import Guest, Reservation


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ["name", "email", "phone", "address"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["guest", "room", "check_in_date", "check_out_date"]
