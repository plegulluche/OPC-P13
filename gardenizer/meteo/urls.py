from django.urls import path
from . import views


urlpatterns = [
    path('meteo-week',views.render_week_forecast_view,name='weekly_forecast'),
    
]