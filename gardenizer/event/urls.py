from django.urls import path
from . import views


urlpatterns = [
    path('event-type', views.select_event_type_view, name='select_event_type'),
    path('add-customer-event', views.add_customer_event_view, name='add_customer_event'),
    path('add-maintenance-event', views.add_maintenance_event_view, name='add_maintenance_event'),
    path('add-customer', views.add_customer_view, name='add_customer'),
]