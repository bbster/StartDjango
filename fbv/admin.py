from django.contrib import admin
from . import models

@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lyrics')
