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
