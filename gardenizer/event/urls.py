from django.urls import path
from . import views


urlpatterns = [
    path(
        "add-customer-event", views.add_customer_event_view, name="add_customer_event"
    ),
    path(
        "add-maintenance-event",
        views.add_maintenance_event_view,
        name="add_maintenance_event",
    ),
    path("event/<int:eventid>/delete", views.delete_event_view, name="delete_event"),
    path(
        "customer-event/<int:eventid>/update",
        views.update_customer_event_view,
        name="update_customer_event",
    ),
    path(
        "maintenance-event/<int:eventid>/update",
        views.update_maintenance_event_view,
        name="update_maintenance_event",
    ),
    path("add-customer", views.add_customer_view, name="add_customer"),
    path(
        "customer/<int:customerid>/delete",
        views.delete_customer_view,
        name="customer_delete",
    ),
    path(
        "customer/<int:customerid>/update",
        views.edit_customer_view,
        name="customer_update",
    ),
    path("success", views.render_update_success_page, name="success"),
]
