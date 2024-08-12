from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ROOM_CAT = (
    ("SIN", "Single"),
    ("DUO", "Double"),
    ("TRI", "Triple"),
    ("DLX", "Deluxe"),
    ("SUT", "Suite"),
)

class Rooms(models.Model):
    category = models.CharField(max_length=3, choices=ROOM_CAT, default="SIN")
    room_no = models.IntegerField(unique=True)
    price = models.IntegerField(default=0)

    class Meta:
        ordering = ['room_no']

    def __str__(self):
        return f"{self.room_no}: {self.category}"


class Bookings(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booked_by")
    room_booked = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="room")
    check_in = models.DateField()
    check_out = models.DateField()
    total_cost = models.IntegerField(default=0)

    class Meta:
        ordering = ['check_in']

    def __str__(self):
        return f"Room: {self.room_booked}, Guest: {self.guest}, Check In: {self.check_in}, Check Out: {self.check_out}"