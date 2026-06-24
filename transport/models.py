from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100) # Gaadi ka naam (e.g., Toyota Corolla)
    model = models.CharField(max_length=50)  # Model (e.g., 2024)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2) # Rate
    is_available = models.BooleanField(default=True) # Kya gaadi available hai?

    def __str__(self):
        return self.name

class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.vehicle.name}"
