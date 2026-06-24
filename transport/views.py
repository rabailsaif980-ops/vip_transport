from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def book_ride(request):
    return render(request, 'booking_form.html')

def send_whatsapp(request):
    if request.method == 'POST':
        # User ka data utha rahe hain
        customer_name = request.POST.get('name')
        destination = request.POST.get('destination')
        car_type = request.POST.get('car')
        
        # Professional variable names
        phone_number = "966599181070" 
        
        # Professional message format
        message = (
            f"New Booking Request%0A%0A"
            f"Customer: {customer_name}%0A"
            f"Destination: {destination}%0A"
            f"Vehicle: {car_type}"
        )
        
        # WhatsApp URL
        whatsapp_url = f"https://wa.me/{phone_number}?text={message}"
        
        return redirect(whatsapp_url)
    
    return redirect('book_ride')