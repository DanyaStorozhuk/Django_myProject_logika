from django import forms
from .models import Booking, Reviews

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time']



class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ім’я'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш відгук'}),
        }