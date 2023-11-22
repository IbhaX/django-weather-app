import requests
from .models import Location, Current, AirQuality

def weather_data(query, aqi):
    aqi = 'yes' if aqi else 'no'
    api_key = "da3eb76c67714939a7a72559230109"
    params = {
        "key": api_key,
        "q": query,
        "aqi": aqi
    }
    url = "https://api.weatherapi.com/v1/current.json"
    
    res = requests.get(url, params=params)
    
    if res.ok:
        return res.json()
    return {"location": {}, "current": {"air_quality": {}}}

def save_weather_data(city_name, user, aqi=False):
    data = weather_data(city_name, aqi=aqi)
    location_data = data.get('location', {})
    current_data = data.get('current', {})
    air_quality_data = current_data.get('air_quality', {})

    # Try to retrieve an existing location with the same name
    location, created = Location.objects.get_or_create(
        user=user,
        name=location_data.get('name'),
        defaults={
            'region': location_data.get('region'),
            'country': location_data.get('country'),
            'lat': location_data.get('lat'),
            'lon': location_data.get('lon'),
            'tz_id': location_data.get('tz_id'),
            'localtime_epoch': location_data.get('localtime_epoch'),
            'localtime': location_data.get('localtime'),
        }
    )

    # If the location already exists, update its fields
    if not created:
        # Update fields other than name
        location.region = location_data.get('region')
        location.country = location_data.get('country')
        location.lat = location_data.get('lat')
        location.lon = location_data.get('lon')
        location.tz_id = location_data.get('tz_id')
        location.localtime_epoch = location_data.get('localtime_epoch')
        location.localtime = location_data.get('localtime')
        location.save()

    # Create or update the air quality data
    air_quality, created = AirQuality.objects.get_or_create(
        user=user,
        defaults={
            'co': air_quality_data.get('co'),
            'no2': air_quality_data.get('no2'),
            'o3': air_quality_data.get('o3'),
            'so2': air_quality_data.get('so2'),
            'pm2_5': air_quality_data.get('pm2_5'),
            'pm10': air_quality_data.get('pm10'),
            'us_epa_index': air_quality_data.get('us-epa-index'),
            'gb_defra_index': air_quality_data.get('gb-defra-index'),
        }
    )

    # If the air quality data already exists, update its fields
    if not created:
        air_quality.co = air_quality_data.get('co')
        air_quality.no2 = air_quality_data.get('no2')
        air_quality.o3 = air_quality_data.get('o3')
        air_quality.so2 = air_quality_data.get('so2')
        air_quality.pm2_5 = air_quality_data.get('pm2_5')
        air_quality.pm10 = air_quality_data.get('pm10')
        air_quality.us_epa_index = air_quality_data.get('us-epa-index')
        air_quality.gb_defra_index = air_quality_data.get('gb-defra-index')
        air_quality.save()

    # Create or update the current data
    current, created = Current.objects.get_or_create(
        location=location,
        last_updated_epoch=current_data.get('last_updated_epoch'),
        defaults={
            'last_updated': current_data.get('last_updated'),
            'temp_c': current_data.get('temp_c'),
            'temp_f': current_data.get('temp_f'),
            'is_day': current_data.get('is_day'),
            'condition_text': current_data.get('condition', {}).get('text'),
            'condition_icon': current_data.get('condition', {}).get('icon'),
            'condition_code': current_data.get('condition', {}).get('code'),
            'wind_mph': current_data.get('wind_mph'),
            'wind_kph': current_data.get('wind_kph'),
            'wind_degree': current_data.get('wind_degree'),
            'wind_dir': current_data.get('wind_dir'),
            'pressure_mb': current_data.get('pressure_mb'),
            'pressure_in': current_data.get('pressure_in'),
            'precip_mm': current_data.get('precip_mm'),
            'precip_in': current_data.get('precip_in'),
            'humidity': current_data.get('humidity'),
            'cloud': current_data.get('cloud'),
            'feelslike_c': current_data.get('feelslike_c'),
            'feelslike_f': current_data.get('feelslike_f'),
            'vis_km': current_data.get('vis_km'),
            'vis_miles': current_data.get('vis_miles'),
            'uv': current_data.get('uv'),
            'gust_mph': current_data.get('gust_mph'),
            'gust_kph': current_data.get('gust_kph'),
        }
    )

    # If the current data already exists, update its fields
    if not created:
        current.last_updated_epoch = current_data.get('last_updated_epoch')
        current.last_updated = current_data.get('last_updated')
        current.temp_c = current_data.get('temp_c')
        current.temp_f = current_data.get('temp_f')
        current.is_day = current_data.get('is_day')
        current.condition_text = current_data.get('condition', {}).get('text')
        current.condition_icon = current_data.get('condition', {}).get('icon')
        current.condition_code = current_data.get('condition', {}).get('code')
        current.wind_mph = current_data.get('wind_mph')
        current.wind_kph = current_data.get('wind_kph')
        current.wind_degree = current_data.get('wind_degree')
        current.wind_dir = current_data.get('wind_dir')
        current.pressure_mb = current_data.get('pressure_mb')
        current.pressure_in = current_data.get('pressure_in')
        current.precip_mm = current_data.get('precip_mm')
        current.precip_in = current_data.get('precip_in')
        current.humidity = current_data.get('humidity')
        current.cloud = current_data.get('cloud')
        current.feelslike_c = current_data.get('feelslike_c')
        current.feelslike_f = current_data.get('feelslike_f')
        current.vis_km = current_data.get('vis_km')
        current.vis_miles = current_data.get('vis_miles')
        current.uv = current_data.get('uv')
        current.gust_mph = current_data.get('gust_mph')
        current.gust_kph = current_data.get('gust_kph')
        current.air_quality = air_quality  # Set the air_quality relationship
        current.save()
