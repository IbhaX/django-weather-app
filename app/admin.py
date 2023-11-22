from django.contrib import admin

from .models import Current, Location, AirQuality



admin.site.register(Current)
admin.site.register(Location)
admin.site.register(AirQuality)