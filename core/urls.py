from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from django.urls import reverse


def sitemap_view(request):
    pages = [
        request.build_absolute_uri(reverse('index')),
        request.build_absolute_uri(reverse('book_ride')),
        request.build_absolute_uri(reverse('contact')),
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    for page in pages:
        xml += f'<url><loc>{page}</loc></url>'

    xml += '</urlset>'

    return HttpResponse(xml, content_type='application/xml')


def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://rabailsaif.pythonanywhere.com/sitemap.xml
"""
    return HttpResponse(content, content_type='text/plain')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('transport.urls')),

    path('sitemap.xml', sitemap_view, name='sitemap'),

    path('robots.txt', robots_txt, name='robots'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )