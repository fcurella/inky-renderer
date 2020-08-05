from django.contrib import admin

from .models import Screen


class ScreenAdmin(admin.ModelAdmin):
    list_display = ("name")


admin.register(Screen, ScreenAdmin)
