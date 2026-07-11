from django.contrib import admin
from .models import Service, Vehicle, Booking, Gallery


# ==========================
# SERVICE ADMIN
# ==========================

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)


# ==========================
# VEHICLE ADMIN
# ==========================

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    fields = (
        "name",
        "seats",
        "luggage_capacity",
        "image",
        "interior",
    )

    list_display = (
        "name",
        "seats",
        "luggage_capacity",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "seats",
    )

    ordering = (
        "name",
    )


# ==========================
# BOOKING ADMIN
# ==========================

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "service",
        "booking_date",
        "pickup_location",
    )

    search_fields = (
        "customer_name",
        "pickup_location",
    )

    list_filter = (
        "service",
        "booking_date",
    )

    ordering = (
        "-booking_date",
    )
    # ==========================
# GALLERY ADMIN
# ==========================

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "title",
    )
