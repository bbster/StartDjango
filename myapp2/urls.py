from django.contrib import admin
from django.urls import path, include
from myapp2 import views

urlpatterns = [
    path('', views.song_list),
    path('detail/<int:pk>', views.songs_detail)
]
