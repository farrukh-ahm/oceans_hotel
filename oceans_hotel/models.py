from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ROOM_CAT = (
    ("SIN", "Single"),
    ("DUO", "Double"),
    ("TRI", "Triple"),
    ("DLX", "Deluxe"),
    ("SUT", "Suite"),
    ("QUN", "Queen"),
    ("KNG", "king"),
    ("VLA", "Villa")
)

class Rooms(models.Model):
    category = models.CharField(max_length=3, choices=ROOM_CAT, default="SIN")
    room_no = models.IntegerField(unique=True)

    class Meta:
        ordering = ['room_no']

    def __str__(self):
        return f"{self.room_no}: {self.category}"

