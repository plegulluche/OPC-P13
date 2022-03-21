from multiprocessing.connection import Client
import pytest
from pytest_django.asserts import assertTemplateUsed
from account.forms import RegisterUserForm
from account.models import Account


@pytest.mark.django_db
def test_user_already_auth_register_view(client,authenticated_user):
    response = client.get('/register/')
    assert response.content.decode('utf8') == 'Vous etes déjà autentifié en tant que foo@gmail.com'


@pytest.mark.django_db
def test_form_in_template_for_get(client):
    response = client.get('/register/')
    assert "registration_form" in response.context


@pytest.mark.django_db
def test_account_registration_view_form_ok(client):
    payload = {
        "email":"testuser@gmail.com",
        "password1":"UnMotDePasse12",
        "password2":"UnMotDePasse12",
        "username":"testuser"
    }
    response = client.post('/register/',payload)
    user = Account.objects.filter(email='testuser@gmail.com').first()
    assert user.email == 'testuser@gmail.com'
    assert response.status_code == 302
    assertTemplateUsed('account/register.html')

@pytest.mark.django_db
def test_account_registration_view_form_not_ok(client):
    payload = {
        "email":'',
        "password1":"",
        "password2":"",
        "username":"testuser"
    }
    form = RegisterUserForm()
    response = client.post('/register/',payload)
    assert response.status_code == 200
    assert "registration_form" in response.context
    assertTemplateUsed('account/register.html')

@pytest.mark.django_db
def test_account_view(client,authenticated_user):
    response = client.get('/account')
    assert response.status_code == 200
    assertTemplateUsed('account/account.html')

@pytest.mark.django_db
def test_form_in_context_get_login_view(client):
    response = client.get('/login/')
    assert 'login_form' in response.context

@pytest.mark.django_db
def test_redirect_if_user_auth_login_view(client,authenticated_user):
    response = client.get('/login/')
    assert response.status_code == 302
    
@pytest.mark.django_db
def test_post_data_is_valid_login_view(client,create_new_user):
    payload = {
        'email':'foo@gmail.com',
        'password':'oAy&mX57qeo&C3cE'
    }
    response = client.post('/login/',payload)
    assert response.status_code == 302

def test_logout_view(client):
    response = client.get('/logout/')
    assert response.status_code == 302
    assertTemplateUsed('website/index.html')

@pytest.mark.django_db   
def test_account_customer_view(client,authenticated_user):
    response = client.get('/account-customer')
    assert response.status_code == 200
    assertTemplateUsed("account/account_customers.html")

@pytest.mark.django_db
def test_account_event_view(client,authenticated_user):
    response = client.get('/account-event')
    assert response.status_code == 200
    assertTemplateUsed("account/account_events.html")