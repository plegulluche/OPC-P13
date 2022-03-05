from datetime import datetime,timezone
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
            data = MeteoData.objects.filter(insee=self.insee)
            return data
        else:
            weather = Weathermanager()
            old_meteo_data = MeteoData.objects.filter(insee=self.insee)
            print(old_meteo_data)
            old_meteo_data.delete()
            weather.get_weekly_forecast(self.insee)
            data = MeteoData.objects.filter(insee=self.insee)
            return data
