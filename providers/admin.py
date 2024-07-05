from django.contrib import admin
from .models import Provider, Area

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'national_code', 'phone_number', 'car_name', 'car_color', 'car_tag', 'get_areas')
    search_fields = ('name', 'last_name', 'national_code', 'phone_number', 'car_name', 'car_color', 'car_tag', 'get_areas')
    def get_areas(self, obj):
        return ", ".join([area.name for area in obj.areas.all()])
    get_areas.short_description = 'Areas'
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)