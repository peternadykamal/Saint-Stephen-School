from django.urls import include, path

from . import profileUrls, tagUrls

urlpatterns = [
    path('u/', include(profileUrls)),
    path('tag/', include(tagUrls)),
]
