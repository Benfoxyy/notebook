from django.contrib import admin
from .models import notes

@admin.register(notes)
class AdminNotes(admin.ModelAdmin):
    list_display=('title',)
    