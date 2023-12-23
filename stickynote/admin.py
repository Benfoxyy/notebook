from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import notes

@admin.register(notes)
class AdminNotes(SummernoteModelAdmin):
    list_display=('title',)
    summernote_fields = ('text',)
    