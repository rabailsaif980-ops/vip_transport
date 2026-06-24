from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book_ride, name='book_ride'),
    path('send-whatsapp/', views.send_whatsapp, name='send_whatsapp'),
]