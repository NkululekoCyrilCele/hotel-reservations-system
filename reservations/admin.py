from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_number", "room_type", "price", "is_available")
    list_filter = ("room_type", "is_available")
    search_fields = ("room_number", "description")


admin.site.register(Room, RoomAdmin)
