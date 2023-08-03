from django.db import models


class Room(models.Model):
    ROOM_TYPES = (
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    )

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(
        max_length=10, choices=ROOM_TYPES, default="single")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_number} - {self.room_type}"

    class Meta:
        ordering = ["room_number"]


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    room_type = models.CharField(
        max_length=10, choices=Room.ROOM_TYPES, default="single")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.guest.name} - Room {self.room.room_number}"

    class Meta:
        ordering = ["-created_at"]
