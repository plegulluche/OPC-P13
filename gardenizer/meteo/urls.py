from django.urls import path
from . import views


urlpatterns = [
    path('meteo-week/',views.get_week_forecast_view,name='weekly_forecast'),
    path('search/',views.search_city,name='search'),
]