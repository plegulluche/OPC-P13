import pytest

from account.models import Account

@pytest.fixture
def authenticated_user(client):
    """create an authenticated user for a test"""
    email = "foo@gmail.com"
    password = "oAy&mX57qeo&C3cE"
    username = "Donaldduck"
    new_user = Account()
    new_user.username = username
    new_user.email = email
    new_user.password = password
    new_user.save()
    new_user.set_password(password)
    new_user.save()
    client.login(email=email,password=password)
    return new_user

@pytest.fixture
def create_new_user(client):
    """create a user for a test"""
    email = "foo@gmail.com"
    password = "oAy&mX57qeo&C3cE"
    username = "Donaldduck"
    new_user = Account()
    new_user.username = username
    new_user.email = email
    new_user.password = password
    new_user.save()
    new_user.set_password(password)
    new_user.save()
    return new_user