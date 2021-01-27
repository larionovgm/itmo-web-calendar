from django.contrib import admin

# Register your models here.
from .models import Calendar
from .models import Event

admin.site.register(Calendar)
admin.site.register(Event)