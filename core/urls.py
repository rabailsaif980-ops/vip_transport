from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transport.urls')),
]

# Ye line Django ko batati hai ke images kahan se uthani hain
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)