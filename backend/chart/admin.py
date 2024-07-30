from django.contrib import admin

from .models import Home, Zodiac, Plant, PlantLayer, Detail, Psychology



@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('persianName', 'nationalName', 'removed_description_tag',)
    list_filter = ('persianName', 'nationalName', 'description',)
    search_fields = ('persianName', 'nationalName', 'description',)
    ordering = ('created_at',)
    


@admin.register(Zodiac)
class ZodiacAdmin(admin.ModelAdmin):
    list_display = ('persianName', 'nationalName', 'sign', 'image_tag', 'removed_description_tag',)
    list_filter = ('persianName', 'nationalName', 'sign', 'description',)
    search_fields = ('persianName', 'nationalName', 'sign', 'description',)
    ordering = ('created_at',)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('persianName', 'nationalName','removed_description_tag', 'get_reinforcement',  'reinDescription','image_tag', )
    list_filter = ('persianName', 'nationalName','description',  'reinDescription', )
    search_fields = ('persianName', 'nationalName','description',  'reinDescription', )
    ordering = ('created_at',)



@admin.register(PlantLayer)
class PlantLayerAdmin(admin.ModelAdmin):
    list_display = ('persianName', 'nationalName', 'removed_description_tag','created_at',)
    list_filter = ('persianName', 'nationalName', 'description','created_at',)
    search_fields = ('persianName', 'nationalName', 'description','created_at',)
    ordering = ('created_at',)



@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('name',  'zodiac','home', 'plant','plantLayer','created_at',)
    list_filter = ('name',  'zodiac','home','plant','plantLayer','created_at',)
    search_fields = ('name',  'zodiac','home','plant','plantLayer','created_at',)
    ordering = ('-created_at',)




@admin.register(Psychology)
class PsychologyAdmin(admin.ModelAdmin):
    list_display = ('name',  'removed_description_tag','created_at',)
    list_filter = ('name',  'description','created_at',)
    search_fields = ('name',  'description','created_at',)
    ordering = ('created_at',)
