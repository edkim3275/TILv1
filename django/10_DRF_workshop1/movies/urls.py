from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_index_or_create),
    path('movies/<int:movie_pk>/', views.movie_detail_or_update_or_delete),
]
