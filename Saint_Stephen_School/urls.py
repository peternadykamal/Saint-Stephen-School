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
  # testing path for playing with templates and components
  urlpatterns += [path('test/', views.renderTestTemplate, name='test-template'),
                  path('testPost/', views.testPost, name='test-post'),
                  path('testGet/', views.testGet, name='test-get'),
                  path('testSearch/', views.testSearch, name='test-search')]
else:
  urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
  urlpatterns += [path(f'{settings.MEDIA_URL}<path:path>/'.lstrip('/'),
                       views.mediaAccess, name='media-access'),]
