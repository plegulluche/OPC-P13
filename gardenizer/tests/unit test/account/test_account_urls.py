from django.urls import reverse, resolve


def test_register():
    path = reverse("register")
    assert path == "/register/"
    assert resolve(path).view_name == "register"