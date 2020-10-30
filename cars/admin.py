from django.contrib import admin
from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('company', 'model', 'year', 'transmission', 'color')
