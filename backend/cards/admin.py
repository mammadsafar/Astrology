from django.contrib import admin
from .models import Card, SocialMedia, Button


@admin.register(Card)
class ProfileAdmin(admin.ModelAdmin):
    model = Card
    list_display = ('user', 'first_name', 'last_name', 'title')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    model = SocialMedia
    list_display = ('card', 'link')


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    model = Button
    list_display = ('card', 'link')
