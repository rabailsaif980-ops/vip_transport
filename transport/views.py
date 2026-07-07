from django.shortcuts import render, redirect
from .models import Car

def index(request):
    cars = Car.objects.all() 
    return render(request, 'transport/index.html', {'cars': cars})

def book_ride(request):
    return render(request, 'transport/booking_form.html')

def send_whatsapp(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        contact_number = request.POST.get('phone')
        pickup_location = request.POST.get('pickup')
        dropoff_location = request.POST.get('destination')
        
        phone_number = "966599181070" 
        
        message = (
            f"--- NEW BOOKING REQUEST ---%0A%0A"
            f"Customer Name: {customer_name}%0A"
            f"Contact Number: {contact_number}%0A"
            f"Pick up Location: {pickup_location}%0A"
            f"Drop off Location: {dropoff_location}"
        )
        
        whatsapp_url = f"https://wa.me/{phone_number}?text={message}"
        return redirect(whatsapp_url)
        
    return redirect('book_ride')

def contact(request):
    return render(request, 'transport/contact.html')