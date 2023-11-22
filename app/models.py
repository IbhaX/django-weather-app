# models.py
from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    tz_id = models.CharField(max_length=255)
    localtime_epoch = models.BigIntegerField()
    localtime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

class Current(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    last_updated_epoch = models.BigIntegerField()
    last_updated = models.DateTimeField()
    temp_c = models.FloatField()
    temp_f = models.FloatField()
    is_day = models.BooleanField()
    condition_text = models.CharField(max_length=255)
    condition_icon = models.URLField()
    condition_code = models.IntegerField()
    wind_mph = models.FloatField()
    wind_kph = models.FloatField()
    wind_degree = models.IntegerField()
    wind_dir = models.CharField(max_length=255)
    pressure_mb = models.FloatField()
    pressure_in = models.FloatField()
    precip_mm = models.FloatField()
    precip_in = models.FloatField()
    humidity = models.IntegerField()
    cloud = models.IntegerField()
    feelslike_c = models.FloatField()
    feelslike_f = models.FloatField()
    vis_km = models.FloatField()
    vis_miles = models.FloatField()
    uv = models.FloatField()
    gust_mph = models.FloatField()
    gust_kph = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class AirQuality(models.Model):
    co = models.FloatField(blank=True, null=True)
    no2 = models.FloatField(blank=True, null=True)
    o3 = models.FloatField(blank=True, null=True)
    so2 = models.FloatField(blank=True, null=True)
    pm2_5 = models.FloatField(blank=True, null=True)
    pm10 = models.FloatField(blank=True, null=True)
    us_epa_index = models.IntegerField(blank=True, null=True)
    gb_defra_index = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
