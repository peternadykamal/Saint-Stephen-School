from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
import os

urlpatterns = [
    path('adminTalmza/', admin.site.urls),
    path('', include('landing.urls')),
    path('u/', include('users.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += [path(f'{settings.MEDIA_URL}<path:path>/'.lstrip('/'), views.mediaAccess, name='media-access'),]
