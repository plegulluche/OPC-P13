from django.urls import path,include
from . import views

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/day/<int:month>/<int:day>', views.single_day_view, name='day'),
]