from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artist_list_or_create),
    path('artists/<int:artist_pk>/', views.artist_detail),
    path('artists/<int:artist_pk>/music/', views.music_create),
    path('artists/music/', views.music_list), 
    path('artists/<int:artist_pk>/music/<int:music_pk>/', views.music_detail_or_update_or_delete),
]
