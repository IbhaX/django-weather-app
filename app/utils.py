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

    location = Location.objects.create(
        name=location_data.get('name'),
        region=location_data.get('region'),
        country=location_data.get('country'),
        lat=location_data.get('lat'),
        lon=location_data.get('lon'),
        tz_id=location_data.get('tz_id'),
        localtime_epoch=location_data.get('localtime_epoch'),
        localtime=location_data.get('localtime'),
    )

    current = Current.objects.create(
        location=location,
        last_updated_epoch=current_data.get('last_updated_epoch'),
        last_updated=current_data.get('last_updated'),
        temp_c=current_data.get('temp_c'),
        temp_f=current_data.get('temp_f'),
        is_day=current_data.get('is_day'),
        condition_text=current_data.get('condition', {}).get('text'),
        condition_icon=current_data.get('condition', {}).get('icon'),
        condition_code=current_data.get('condition', {}).get('code'),
        wind_mph=current_data.get('wind_mph'),
        wind_kph=current_data.get('wind_kph'),
        wind_degree=current_data.get('wind_degree'),
        wind_dir=current_data.get('wind_dir'),
        pressure_mb=current_data.get('pressure_mb'),
        pressure_in=current_data.get('pressure_in'),
        precip_mm=current_data.get('precip_mm'),
        precip_in=current_data.get('precip_in'),
        humidity=current_data.get('humidity'),
        cloud=current_data.get('cloud'),
        feelslike_c=current_data.get('feelslike_c'),
        feelslike_f=current_data.get('feelslike_f'),
        vis_km=current_data.get('vis_km'),
        vis_miles=current_data.get('vis_miles'),
        uv=current_data.get('uv'),
        gust_mph=current_data.get('gust_mph'),
        gust_kph=current_data.get('gust_kph'),
        user=user,  
    )

    air_quality = AirQuality.objects.create(
        co=air_quality_data.get('co'),
        no2=air_quality_data.get('no2'),
        o3=air_quality_data.get('o3'),
        so2=air_quality_data.get('so2'),
        pm2_5=air_quality_data.get('pm2_5'),
        pm10=air_quality_data.get('pm10'),
        us_epa_index=air_quality_data.get('us-epa-index'),
        gb_defra_index=air_quality_data.get('gb-defra-index'),
        user=user,  
    )