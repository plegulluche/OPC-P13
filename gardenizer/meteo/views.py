from django.http import JsonResponse
from event.models import City
from .utils.meteo_data_manager import (
    CacheManager,jsonify_payload
    )


def get_week_forecast_view(request):
    
    if request.method == 'POST':
        city = City.objects.get(name=request.body.decode('utf-8'))
        weather = CacheManager(city.insee)
        meteo_week = weather.get_meteo_data()
        payload = jsonify_payload(meteo_week)
        
        return JsonResponse({'status':200,'meteo_week':payload})

def search_city(request):
    city = request.GET.get('city')
    payload = []
    if city:  
        city_objs = City.objects.filter(name__icontains=city.capitalize())
        
        for city_obj in city_objs:
            payload.append(city_obj.name)
    return JsonResponse({'status':200,'data':payload})
        