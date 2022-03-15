from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.registration_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("account", views.account_view, name="account"),
    path("account-customer", views.account_customer_view,name="account_customer"),
    path("account-event", views.account_events_view,name="account_event"),
  
]