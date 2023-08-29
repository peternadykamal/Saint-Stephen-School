from django.urls import path

from users import views

urlpatterns = [
    # add and update tag page on root of tag
    path('',  views.tagsPage, name='tag-page'),
    path('get/', views.getTag, name='get-tag'),
    path('updateHierarchy/', views.updateHierarchy, name='update-hierarchy'),
    path('update/', views.updateTag, name='update-tag'),
    path('add/', views.addTag, name='add-tag'),
    path('delete/<uuid:tag_id>/', views.deleteTag, name='delete-tag')
]
