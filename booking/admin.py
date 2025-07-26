from django.contrib import admin 
from booking.models import Booking, Room, Guest, Service
# Register your models here.


admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Service)