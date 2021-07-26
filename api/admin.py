from django.contrib import admin

# Register your models here.
from api.models import Ship, Position


class ShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'imo')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('ship', 'latitude', 'longitude' )

admin.site.register(Ship, ShipAdmin)
admin.site.register(Position, PositionAdmin)