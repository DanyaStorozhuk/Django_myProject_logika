from django.shortcuts import render, redirect
from .forms import BookingForm, ReviewsForm
from .models import Room
from django.http import HttpResponse
from booking.models import Booking, Room, Reviews
# Create your views here.

def room_list(request):
    # за допомогою цієї функції ми отримаємо всі кімнати з бази
    rooms = Room.objects.all()
    # Відображаємо шаблон з даними
    return render(request, 'room_list.html', {'rooms': rooms})


def booking_view(request):
    # Перевіряємо, чи надійшов POST (тобто чи користувач натиснув "відправити" у формі)
    if request.method == 'POST':
        # Створюємо об'єкт форми з даними, які користувач надіслав через форму
        form = BookingForm(request.POST)

        # Перевіряємо, чи форма заповнена правильно ( наприклад чи всі обов'язкові поля заповнено та чи правильний формат дати)
        if form.is_valid():
            # зберігаємо дані з форми в базу даних (тобто створюємо новий запис бронювання)
            form.save()

            # переадресовуємо користувача на сторінку зі списком кімнат після того як бронювання успішно пройшло
            return redirect('room_list')
        
    else:
        # Якщо запит не POST (наприклад GET - користувач просто відкрив сторінку), то створюємо порожню форму 
        form = BookingForm()

    # Повертаємо HTML - сторінку з формою (booking_form.html), передаючи в шаблон об'єкт форми 
    return render(request, 'booking_form.html', {'form': form})

def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(number=room_number)

        except ValueError:
            return HttpResponse(
                "Wrong value for room number!",
                status = 400
                )
        except Room.DoesNotExist:
            return HttpResponse(
                "This room number doesn't exist",
                status = 404
            )
        booking = Booking.objects.create(
            user = request.user,
            room = room,
            start_time=start_time,
            end_time=end_time
            ).save()
        return redirect("booking-details")
    else:
        return render(request, template_name="new_booking_form2.html")
    

def booking_details(request):
    try:
        booking = Booking.objects.filter(user = request.user.id)
        context = {
            "bookings": booking

        }
        
        return render(request, template_name="booking_details.html", context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            "This booking doens't exist",
            status=404
        )

def reviews_list(request):
    reviews = Reviews.objects.order_by('-created_at')  # Новіші зверху

    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews_list')
    else:
        form = ReviewsForm()

    return render(request, 'reviews_list.html', {'reviews': reviews, 'form': form})