from django.urls import reverse, resolve

def test_calendar():
    path = reverse("calendar")
    assert path == "/calendar/"
    assert resolve(path).view_name == "calendar"

def test_calendar_day():
    path = reverse('day',kwargs={"month":2,"day":2})
    assert path == '/calendar/day/2/2'
    assert resolve(path).view_name == "day"