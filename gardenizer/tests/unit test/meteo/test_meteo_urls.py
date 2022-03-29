from django.urls import reverse, resolve


def test_meteo_week():
    path = reverse("weekly_forecast")
    assert path == "/meteo-week/"
    assert resolve(path).view_name == "weekly_forecast"


def test_search():
    path = reverse("search")
    assert path == "/search/"
    assert resolve(path).view_name == "search"
