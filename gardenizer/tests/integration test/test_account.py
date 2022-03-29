import pytest
from account.views import (account_view, login_view, logout_view,
                           registration_view)
from django.contrib import auth
from django.contrib.auth import logout
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_login_route(client):
    """
    First we test if the 'login' route maps to 'login_view', then we check if the login_view
    renders the correct template ( account/login.html )
    Then, we create a temporary user, and login with those credentials and see whether user 
    is redirected to '/' route if the login was successful
    """
    #Testing if login route maps to login_view
    url = reverse('login')
    assert resolve(url).func ,login_view
    
    #Testing if the 'login_view' renders the correct template (account/login.html)
    response = client.get(reverse('login'))
    assertTemplateUsed(response,'account/login.html')
    
    credentials = {
        "email":"testuser@gmail.com",
        "password1":"UnMotDePasse12",
        "password2":"UnMotDePasse12",
        "username":"testuser"
    }
    
    temp_user = client.post("/register/",credentials)
    
    #We logout the user after creating it because of the redirection on the mainpage afetr creation
    response = client.get(reverse('logout'))
    assert response.status_code == 302
    
    #We log in the user and see if it properly redirects us to the mainpage
    response = client.post(reverse("login"),{"email":"testuser@gmail.com","password":"UnMotDePasse12"})
    
    
    assert temp_user.status_code == 302
    assert temp_user.url == reverse('mainpage')
    
    user = auth.get_user(client)
    assert user.is_authenticated
    
@pytest.mark.django_db
def test_login_route_failed(client):
    """
    Testing if the user enters the false credentails then the user stays on the 'login' route,
    and is asked to re-enter the correct credentials
    """
    response = client.post(reverse('login'),{'email':"Notagoodone","password":"Notagoodone"})
    assertTemplateUsed(response,'account/login.html')
    
@pytest.mark.django_db
def test_register_route(client):

    """
    Test approach starts with testing if the 'registration' route maps to 'registration_view'. Then we test 
    if the registration_view renders the correct template ( account/register.html ) with correct Form ( RegisterUserForm ).
    After that we create a temporary user, by using our 'register' route and checking if redirects the user to 
    the 'mainpage' route, if everything went fine.
    """

    # Testing if the 'register' route maps to 'registration_view'
    url = reverse('register')
    assert resolve(url).func, registration_view

    # Testing if the SignUpView renders the correct template ( account/register.html ) with correct Form ( RegisterUserForm )
    response = client.get(reverse('register'))
    assert response.status_code == 200
    assert "registration_form" in response.context
    assertTemplateUsed(response, 'account/register.html')

    credentials = {
        "email":"testuser@gmail.com",
        "password1":"UnMotDePasse12",
        "password2":"UnMotDePasse12",
        "username":"testuser"
    }
    # creating a temporary user and testing if the user gets redirected to 'mainpage' route if signup was successful
    response = client.post(reverse('register'), credentials)
    assert response.status_code == 302
    assert response.url == reverse('mainpage')
    
@pytest.mark.django_db
def test_signup_route_failed(client):

    """
    Testing 'register' route with the wrong credentials and testing if user stays on the 'register' 
    route if the registration process failed
    """

    credentials = {
        "email":"testuser@gmail.com",
        "password1":"UnMotDePasse12",
        "password2":"", #password not matching
        "username":"testuser"
    }
    
    response = client.post(reverse('register'), credentials)
    assertTemplateUsed(response, 'account/register.html')
    
@pytest.mark.django_db
def test_logout_route(client):

    """
    First we test if 'logout' route maps to the 'logout_view' or not, then we test if the user is 
    properly logged out and is redirected to 'home' route
    """
    
    # Testing if the 'logout' route maps to 'logout_view'
    url = reverse('logout')
    assert resolve(url).func, logout_view

    # Testing if the user is logged out properly and is redirected to 'mainpage' route
    response = client.get(reverse('logout'))
    assert response.status_code == 302
    assert response.url == reverse('mainpage')
    
@pytest.mark.django_db
def test_account_route(client):

    """
    First we test if 'account' route  maps to 'account_view', then we login with a temporary user and 
    access the account route and test if the correct template ( account.html ) was rendered
    """
    
    # Testing if the 'account' route maps to 'account_view'
    url = reverse('account')
    assert resolve(url).func, account_view

    credentials = {
        "email":"testuser@gmail.com",
        "password1":"UnMotDePasse12",
        "password2":"UnMotDePasse12",
        "username":"testuser"
    }
    temp_user = client.post(reverse('register'), credentials)
    client.post(reverse('login'), {"email":"testuser@gmail.com", "password":"UnMotDePasse12"})

    # Testing if the account_view renders correct template ( account.html )
    response = client.get(reverse('account'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'account/account.html')
    
@pytest.mark.django_db
def test_profile_route_failed(client):

    """
    Testing if the user is redirected to 'register' route if the user is not authenticated and is 
    trying to access the profile
    """

    response = client.get(reverse('account'))
    assert response.status_code == 302
