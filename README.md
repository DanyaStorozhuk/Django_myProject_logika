# 🏨 Hotel Booking System

This is a Django-based web application for people who want to book a hotel room.
Users can reserve a room at a convenient time and desired location,
check the availability of rooms, and view booking details if needed.

---

## 🔧 Features

- **👤 User Authentication:** Room Browsing: View available rooms with descriptions (price, city, desired room).
- **🛏️ Room Browsing:** View available rooms with details (capacity, price, location).
- **📆 Booking System:** Authenticated users can book rooms (no overlapping bookings).
- **🕓 Booking History:** View past and upcoming bookings.
- **📝 Reviews** – Users can leave reviews for rooms they have booked.  
---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML (Django templates) and Bootstrap
- **Authentication:** Django built-in auth system with custom user model
---

## 🚀 Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/DanyaStorozhuk/Django_myProject_logika.git
    cd Django_myProject_logika
    ```

2. **Set Up a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    Install Dependencies:
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser (Optional)**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```


Access the application at http://127.0.0.1:8000

# Project Structure

- `hotel_system/`: Main project directory with settings and URL configurations.  
- `author_system/`: Handles user authentication (register, login, logout).  
- `booking/`: Manages room browsing, booking, and history functionalities.  

## Templates:
- `booking_details.html`: Page that displays the user, their room, and the duration of their stay.
- `booking_form.html`: Main page that greets the user with buttons; the background is taken from the `layout.html` file.
- `header.html`: Page containing template text.
- `layout_room_info.html`: Background layout inherited by the `new_booking_form2.html` file.
- `layout_room_list.html`: Background layout inherited by the `room_list.html` file.
- `reviews_list.html`: View for the user to write a review.
- `auth_system/register.html`: User registration form.


## Models:

- **CustomUser:** Extends Django's AbstractUser with additional fields (phone number).  
- **Room:** Stores room details (number, capacity, location, price).  
- **Booking:** Tracks user bookings with references to users and rooms.  
- **Guest:** Guest model containing fields (first name, last name, email, phone number, passport, and check-in date).  
- **Service:** Additional services (name and price).  
- **Reviews:** User reviews (name, text (review), and date of submission).  


## URL Structure

- `/` — Home page.  
- `/rooms/` — List of all rooms.  
- `/book-room/` — Alternative booking method without using the standard Django form.  
- `/booking-details/` — View the user's booking details.  
- `/reviews_list/` — View and add user reviews.  
- `/admin/` — Django Admin Panel.  
- `/register/` — User registration.  
- `/login/` — User login.

## Usage

- **Register or Log In**: Create an account or log in to access booking features.  
- **View Room List**: Use one of the main buttons to see available rooms.  
- **Book a Room**: Select a room (number) and specify check-in/check-out dates to make a booking.  
- **View Booking History**: Check past and upcoming bookings in the "User Details" section.  
- **Add Reviews**: Use the option to write your own review by providing your name.

## Future Improvements

- Expand the functionality  
- Implement pagination for room listings and booking history  
- Add a room availability calendar  
- Support multiple languages