import requests
import os

from meteo.models import MeteoData

class Weathermanager:
    """
    Class managing our Api call to the weather api.
    """
    
    
    def __init__(self):
        pass

    def get_weekly_forecast(self,city_code):
        """Get 15 days forecast for a specific city, works for french cities only.
        takes insee code of the city as a param.

        Args:
            city_code (int): code insee of the city
        """
        

        url = f"https://api.meteo-concept.com/api/forecast/daily?&insee={city_code}&world=false"
        header = {"Authorization":os.environ.get("API_METEO_KEY")}
        response = requests.get(url,headers=header)
        data = response.json()
        for each_day in data["forecast"]:
            meteo = MeteoData()
            meteo.day = each_day["day"]
            meteo.weather = each_day["weather"]
            meteo.tmin = each_day["tmin"]
            meteo.tmax = each_day["tmax"]
            meteo.probarain = each_day["probarain"]
            meteo.probafrost = each_day["probafrost"]
            meteo.probawind = each_day["probawind70"]
            meteo.datetime = each_day["datetime"]
            meteo.insee = city_code
            meteo.save()