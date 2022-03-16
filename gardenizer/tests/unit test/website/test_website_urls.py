from django.urls import reverse, resolve

def test_meteo_week():
    path = reverse("mainpage")
    assert path == "/"
    assert resolve(path).view_name == "mainpage"
    
