from datetime import timezone
from django.utils import timezone
from meteo.models import MeteoData
from .api import Weathermanager

class CacheManager():
    
    def __init__(self,insee):
        self.insee = insee
        
    def _check_if_data_in_db(self):
        current_datetime_aware = timezone.localtime(timezone.now())
        current_date_aware = current_datetime_aware.date()
        get = MeteoData.objects.filter(day=0).filter(insee=self.insee).first()
        if get:
            if current_date_aware == get.datetime.date():
                return True
            else:
                return False
        else:
            return False
    
    def get_meteo_data(self):
        validator = self._check_if_data_in_db()
        if validator:
            print('API CALL NOT MADE')
            data = MeteoData.objects.filter(insee=self.insee)
            return data
        else:
            print('API CALL MADE')
            weather = Weathermanager()
            old_meteo_data = MeteoData.objects.filter(insee=self.insee)
            old_meteo_data.delete()
            weather.get_weekly_forecast(self.insee)
            data = MeteoData.objects.filter(insee=self.insee)
            return data
        
def jsonify_payload(weather_obj_list):
    payload = {}
    for day in weather_obj_list:
        payload[f'day{day.day}'] = {
            'day': day.day,
            'weather':day.weather,
            'tmin':day.tmin,
            'tmax':day.tmax
        }
    return payload

def get_meteo_and_city_for_an_event(events,day,month):
    event_images_codes = {}
    for event in events:
        city = event.customer.city.insee
        print('CITY : ',city)
        get_meteo = CacheManager(city)
        meteo_data = get_meteo.get_meteo_data()
        meteo = MeteoData.objects.filter(datetime__day=day,insee=city)
        print(meteo)
        if meteo:
            weathercode = meteo[0].weather
            print('WEATHER CODE : ', weathercode)
            weather_image_code = _transform_weather_code_to_img_code(weathercode)
            link_to_img = f'images/{weather_image_code}.svg'
        else:
            weathercode = 0
            print('WEATHER CODE : ', weathercode)
            weather_image_code = _transform_weather_code_to_img_code(weathercode)
            link_to_img = f'images/{weather_image_code}.svg'
        event_images_codes[f'{event.id}'] = [event.id,link_to_img]
                       
    return event_images_codes

def _transform_weather_code_to_img_code(weathercode):
    nbForCloudy = [2,3,4,5]
    nbCloudSun = [1,235]
    nbSun = [0]
    nbSunSnow = [220,221,222]
    nbSunRain = [210,211,212]
    nbCloudRain = [10,11,13,16,30,31,12,14,15,32,40,41,42,43,44,45,46,47,48]
    nbStorm = [100,101,102,103,104,105,106,107,108,120,121,122,
                123,124,125,126,127,128,130,131,132,133,134,135,136,137,138]
    nbSnow = [20,21,22,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,142]
    if weathercode in nbForCloudy:
        return 1
    elif weathercode in nbCloudSun:
        return 2
    elif weathercode in nbSunSnow:
        return 3
    elif weathercode in nbSunRain:
        return 4
    elif weathercode in nbCloudRain:
        return 5
    elif weathercode in nbStorm:
        return 6
    elif weathercode in nbSnow:
        return 7
    else:
        return 8