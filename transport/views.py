from django.shortcuts import render, redirect
from .models import Vehicle, Service


def index(request):
    vehicles = Vehicle.objects.all()
    services = Service.objects.all()

    return render(
        request,
        'transport/index.html',
        {
            'vehicles': vehicles,
            'services': services
        }
    )


def book_ride(request):
    return render(request, 'transport/booking_form.html')


def send_whatsapp(request):

    if request.method == 'POST':

        customer_name = request.POST.get('name')
        contact_number = request.POST.get('phone')
        pickup_location = request.POST.get('pickup')
        dropoff_location = request.POST.get('destination')

        travel_date = request.POST.get('travel_date')
        pickup_time = request.POST.get('pickup_time')
        vehicle = request.POST.get('vehicle')
        passengers = request.POST.get('passengers')
        special_request = request.POST.get('special_request')

        phone_number = "966599181070"

        message = (
            f"🚖 *NEW VIP TRANSPORT BOOKING*%0A%0A"
            f"👤 Name: {customer_name}%0A"
            f"📞 Phone: {contact_number}%0A%0A"

            f"📍 Pickup: {pickup_location}%0A"
            f"📍 Drop-off: {dropoff_location}%0A%0A"

            f"📅 Travel Date: {travel_date}%0A"
            f"⏰ Pickup Time: {pickup_time}%0A%0A"

            f"🚘 Vehicle: {vehicle}%0A"
            f"👥 Passengers: {passengers}%0A%0A"

            f"📝 Special Request:%0A{special_request}"
        )

        whatsapp_url = f"https://wa.me/{phone_number}?text={message}"

        return redirect(whatsapp_url)

    return redirect('book_ride')


def contact(request):
    return render(request, 'transport/contact.html')