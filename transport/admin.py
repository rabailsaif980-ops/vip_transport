from django.contrib import admin
from .models import Car, Booking  # Yahan 'Car' likhna hai, 'Vehicle' nahi

admin.site.register(Car)
admin.site.register(Booking)