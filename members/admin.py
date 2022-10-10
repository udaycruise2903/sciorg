from django.contrib import admin

from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "qualification","profession", "designation", "description")

admin.site.register(Member, MemberAdmin)
