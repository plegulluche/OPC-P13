from django.shortcuts import render
from event.models import City
from .management.meteo_data_manager import CacheManager



def render_week_forecast_view(request):
    message = "Entrez le nom d'une ville et selectionnez la dans le menu ci-dessous"
    q = request.GET.get('q')
    if q:
        cities = City.objects.filter(name__startswith=q.capitalize())
        if cities:
            context = {"cities":cities}
            return render(request, "website/index.html",context)
        else:
            context = {"message":message}
            return render(request,"website/index.html",context)
    if request.method == 'POST':
        city = City.objects.get(pk=request.POST.get('city'))
        weather = CacheManager(city.insee)
        meteo_week = weather.get_meteo_data()
        
        context = {"meteo_week":meteo_week}
        return render(request, "website/index.html",context)
    context = {"message":message}
    return render(request,"website/index.html",context)