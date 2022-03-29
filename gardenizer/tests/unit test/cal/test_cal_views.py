import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse


@pytest.mark.django_db
def test_get_calendat_view(
    client,
    authenticated_user,
):
    """testing get method for the calendar view"""
    response = client.get("/calendar/")
    assert response.status_code == 200
    assertTemplateUsed("cal/cal.html")


@pytest.mark.django_db
def test_get_single_day_view(client, authenticated_user):
    """test get method for single day view for cal app"""
    response = client.get(reverse("day", kwargs={"month": 4, "day": 2}))
    assert response.status_code == 200
    assertTemplateUsed("cal/single_day.html")
