from django.db import models
from django.conf import settings
 
class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Room #{self.number} - {self.capacity} - {self.price}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]



class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings", null=True)
    room =  models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings", null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    creation_time = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.room}"



    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_time"]

class Guest(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    passport = models.CharField(max_length=30)
    createt_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.passport})" 
    
        
class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"
    
class Reviews(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.text}"