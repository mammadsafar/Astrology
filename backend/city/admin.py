from django.contrib import admin

from .models import Country, Province, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'english_name', 'code', 'latitude', 'longitude', 'created_at', 'updated_at']
    search_fields = ['name', 'english_name', 'code']
    list_filter = ['name', 'english_name', 'code', 'latitude', 'longitude']


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', 'english_name', 'country', 'latitude', 'longitude', 'created_at', 'updated_at']
    search_fields = ['name', 'english_name']
    list_filter = ['name', 'english_name', 'latitude', 'longitude']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'english_name', 'province', 'latitude', 'longitude', 'created_at', 'updated_at']
    search_fields = ['name', 'english_name']
    list_filter = ['name', 'english_name', 'province', 'latitude', 'longitude']



