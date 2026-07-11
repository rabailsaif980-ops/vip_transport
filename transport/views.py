from django.shortcuts import render, redirect
from .models import Vehicle, Service, Gallery
from urllib.parse import quote

def index(request):
    vehicles = Vehicle.objects.all()
    services = Service.objects.all()
    gallery = Gallery.objects.all()

    return render(
        request,
        'transport/index.html',
        {
            'vehicles': vehicles,
            'services': services,
            'gallery': gallery,
        }
    )

def book_ride(request):
    return render(request, 'transport/booking_form.html')


def send_whatsapp(request):

    if request.method == "POST":

        customer_name = request.POST.get("name")
        contact_number = request.POST.get("phone")
        pickup_location = request.POST.get("pickup")
        dropoff_location = request.POST.get("destination")

        travel_date = request.POST.get("date")
        pickup_time = request.POST.get("time")
        vehicle = request.POST.get("vehicle")
        passengers = request.POST.get("passengers")
        special_request = request.POST.get("request")

        phone_number = "966599181070"

        message = f"""
🚖 *NEW VIP TRANSPORT BOOKING*

👤 Name: {customer_name}
📞 Phone: {contact_number}

📍 Pickup Location:
{pickup_location}

🏁 Drop-off Location:
{dropoff_location}

📅 Pickup Date: {travel_date}
🕒 Pickup Time: {pickup_time}

🚘 Selected Vehicle:
{vehicle}

👥 Passengers:
{passengers}

📝 Special Request:
{special_request if special_request else 'None'}
"""

        whatsapp_url = f"https://wa.me/{phone_number}?text={quote(message)}"

        return redirect(whatsapp_url)

    return redirect("book_ride")


def contact(request):
    return render(request, "transport/contact.html")