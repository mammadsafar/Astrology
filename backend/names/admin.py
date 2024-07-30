from django.contrib import admin

from .models import Name



@admin.register(Name)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'persian_name', 'gender', 'desteni_number', 'motivation_number', 'country', 'nationality', 'Usage_percentage', 'pronunciation', 'meaning', 'created_at')
    list_filter = ('name', 'persian_name', 'gender', 'desteni_number', 'motivation_number', 'country', 'nationality', 'Usage_percentage', 'pronunciation', 'meaning', 'created_at')
    search_fields = ('name', 'persian_name', 'gender', 'desteni_number', 'motivation_number', 'country', 'nationality', 'Usage_percentage', 'pronunciation', 'meaning', 'created_at')
    ordering = ('name','created_at', 'Usage_percentage')
    