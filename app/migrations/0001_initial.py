# Generated by Django 4.2.7 on 2023-11-22 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AirQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co', models.FloatField(blank=True, null=True)),
                ('no2', models.FloatField(blank=True, null=True)),
                ('o3', models.FloatField(blank=True, null=True)),
                ('so2', models.FloatField(blank=True, null=True)),
                ('pm2_5', models.FloatField(blank=True, null=True)),
                ('pm10', models.FloatField(blank=True, null=True)),
                ('us_epa_index', models.IntegerField(blank=True, null=True)),
                ('gb_defra_index', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('tz_id', models.CharField(max_length=255)),
                ('localtime_epoch', models.BigIntegerField()),
                ('localtime', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated_epoch', models.BigIntegerField()),
                ('last_updated', models.DateTimeField()),
                ('temp_c', models.FloatField()),
                ('temp_f', models.FloatField()),
                ('is_day', models.BooleanField()),
                ('condition_text', models.CharField(max_length=255)),
                ('condition_icon', models.URLField()),
                ('condition_code', models.IntegerField()),
                ('wind_mph', models.FloatField()),
                ('wind_kph', models.FloatField()),
                ('wind_degree', models.IntegerField()),
                ('wind_dir', models.CharField(max_length=255)),
                ('pressure_mb', models.FloatField()),
                ('pressure_in', models.FloatField()),
                ('precip_mm', models.FloatField()),
                ('precip_in', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('cloud', models.IntegerField()),
                ('feelslike_c', models.FloatField()),
                ('feelslike_f', models.FloatField()),
                ('vis_km', models.FloatField()),
                ('vis_miles', models.FloatField()),
                ('uv', models.FloatField()),
                ('gust_mph', models.FloatField()),
                ('gust_kph', models.FloatField()),
                ('air_quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.airquality')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location')),
            ],
        ),
    ]
