from django.urls import path
from booking import views

urlpatterns = [
    path("rooms/", views.room_list, name="rooms"),
    path("", views.booking_view, name="booking"),
    path("book-room/", views.book_room, name="book-room"),
    path("booking-details/", views.booking_details, name="booking-details"),
]