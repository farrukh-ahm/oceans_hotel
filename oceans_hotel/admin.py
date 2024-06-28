from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    model = Rooms
    search_fields = ['room_no', 'category']
    list_filter = ['category']