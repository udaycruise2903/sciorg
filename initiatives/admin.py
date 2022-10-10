from django.contrib import admin

from .models import Initiative


class InitiativeAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

admin.site.register(Initiative, InitiativeAdmin)
