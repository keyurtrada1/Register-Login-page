from django.contrib import admin
from .models import registertable

class showregistertable(admin.ModelAdmin):
    list_display = ["name","email","phone", "password"]
admin.site.register(registertable,showregistertable)
