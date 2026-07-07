from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    exterior_image = models.ImageField(upload_to='cars/')
    interior_image = models.ImageField(upload_to='cars/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    BOOKING_TYPE = (
        ('Trip', 'Per Trip'),
        ('Hourly', 'Hourly Basis'),
        ('12hrs', '12 Hours Full Day'),
    )
    
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    booking_type = models.CharField(max_length=10, choices=BOOKING_TYPE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    # Ye change kiya hai taake user date khud select kar sake
    booking_date = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.car.name}"
