from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Dancer


@admin.register(Dancer)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('dancer_id', 'name', 'position', 'number')