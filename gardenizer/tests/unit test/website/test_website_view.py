from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

CLIENT = Client()

def test_mainpage_view():
    response = CLIENT.get(reverse('mainpage'))
    assert response.status_code == 200
    assertTemplateUsed(response,'website/mainpage.html')
    
def test_legals_page_view():
    response = CLIENT.get(reverse('legals'))
    assert response.status_code == 200
    assertTemplateUsed(response,'website/legals.html')
    
def test_about_page_view():
    response = CLIENT.get(reverse('about'))
    assert response.status_code == 200
    assertTemplateUsed(response,'website/about.html')