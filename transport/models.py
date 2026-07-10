from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()
    icon_or_image = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return self.title

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField()
    luggage_capacity = models.IntegerField()
    image = models.ImageField(upload_to='vehicles/')
    # Interior image ka option add kar diya
    interior = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking_date = models.DateField()
    # pickup_location ka field add kar diya taake error khatam ho jaye
    pickup_location = models.CharField(max_length=255, default="Not specified")
    
    def __str__(self):
        return self.customer_name