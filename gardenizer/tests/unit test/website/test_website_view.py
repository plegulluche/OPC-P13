from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

CLIENT = Client()

def test_mainpage_view():
    response = CLIENT.get(reverse('mainpage'))
    assert response.status_code == 200
    assertTemplateUsed(response,'website/index.html')