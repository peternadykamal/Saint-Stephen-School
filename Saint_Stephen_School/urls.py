from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminTalmza/', admin.site.urls),
    path('', include('landing.urls')),
    path('u/', include('users.urls')),
]
