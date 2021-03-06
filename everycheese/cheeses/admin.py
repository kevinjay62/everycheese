from django.contrib import admin

from .models import Cheese


@admin.register(Cheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'country_of_origin']
