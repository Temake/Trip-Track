from django.contrib import admin

# Register your models here.
from .models import Trip,Note

admin.site.register(Trip)
admin.site.register(Note)