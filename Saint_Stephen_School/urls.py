from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
    path('adminTalmza/', admin.site.urls),
    path('', include('landing.urls')),
    path('u/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
