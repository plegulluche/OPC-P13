from django.urls import reverse, resolve


def test_mainpage_url():
    path = reverse("mainpage")
    assert path == "/"
    assert resolve(path).view_name == "mainpage"


def test_legal_page_url():
    path = reverse("legals")
    assert path == "/legals"
    assert resolve(path).view_name == "legals"


def test_about_page_url():
    path = reverse("about")
    assert path == "/about"
    assert resolve(path).view_name == "about"
