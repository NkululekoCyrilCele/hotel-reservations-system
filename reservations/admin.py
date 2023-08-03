from django.contrib import admin
from .models import Room, Guest, Reservation


class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_number", "room_type", "price", "is_available")
    list_filter = ("room_type", "is_available")
    search_fields = ("room_number", "description")


admin.site.register(Room, RoomAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "address", "room_type")
    search_fields = ("name", "email", "phone", "room_type")


admin.site.register(Guest, GuestAdmin)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("guest", "room", "check_in_date",
                    "check_out_date", "created_at")
    list_filter = ("check_in_date", "check_out_date", "created_at")
    search_fields = ("guest__name", "room__room_number")


admin.site.register(Reservation, ReservationAdmin)
