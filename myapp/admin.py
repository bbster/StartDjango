from django.contrib import admin
from . import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'picture', 'author', 'email', 'describe')
