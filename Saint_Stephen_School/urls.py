import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('adminTalmza/', admin.site.urls),
    path('', include('landing.urls')),
    path('', include('users.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
  urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
  urlpatterns += [path(f'{settings.MEDIA_URL}<path:path>/'.lstrip('/'),
                       views.mediaAccess, name='media-access'),]
