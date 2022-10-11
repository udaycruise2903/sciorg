from django.contrib import admin

from .models import Event, EventCrew


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "organiser", "initiative","start_time", "end_time", "start_date","end_date", "description")

class EventCrewAdmin(admin.ModelAdmin):
    list_display = ("event", "member")

admin.site.register(Event, EventAdmin)
admin.site.register(EventCrew, EventCrewAdmin)
