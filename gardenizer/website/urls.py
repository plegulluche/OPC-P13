from django.urls import path

from . import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("legals", views.legals_page_view, name="legals"),
    path("about", views.about_page_view, name="about"),
]
