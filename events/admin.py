from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "organiser","start_time", "end_time", "start_date","end_date", "description")

admin.site.register(Event)
