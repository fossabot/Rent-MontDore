from django.shortcuts import render, redirect

# Create your views here.

from .forms import BookingForm
from .models import Booking

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            coming_date = form.cleaned_data['coming_date']
            leaving_date = form.cleaned_data['leaving_date']
            email_address = form.cleaned_data['email_address']
            therapy = form.cleaned_data['therapy']

            free = True
            for booking in Booking.objects.all():
                if booking.coming_date <= coming_date <= booking.leaving_date:
                    free = False
                if booking.coming_date <= leaving_date <= booking.leaving_date:
                    free = False
                if coming_date <= booking.coming_date <= leaving_date:
                    free = False

            duplicate = False
            for booking in Booking.objects.filter(last_name=last_name, first_name=first_name):  # Same names
                if coming_date == booking.coming_date:
                    duplicate = True
                elif not booking.leaving_date < coming_date:
                    duplicate = True
                if email_address != booking.email_address:
                    pass  # Costumer change it email address

            if not free and not duplicate:
                msg = "L'appartement n'est pas libre, désolé."
            elif duplicate:
                msg = 'Vous avez déjà réserver pour ces dates.'
            else:
                new_booking = Booking(
                    last_name=last_name,
                    first_name=first_name,
                    coming_date=coming_date,
                    leaving_date=leaving_date,
                    email_address=email_address,
                    therapy=therapy
                )
                new_booking.save()
                msg = 'Votre réservation a été prise en compte !'
        else:
            msg = 'Le formulaire est invalide.'
    else:
        form = BookingForm()
        msg = "Veuillez remplir le formulaire:"

    return render(request, 'booking/booking.html', locals())

def calendar(request):
    bookings = Booking.objects.order_by('coming_date')
    admin = False
    admin = True
    return render(request, 'booking/calendar.html', locals())
