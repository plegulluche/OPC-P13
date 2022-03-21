import pytest
from account.models import Account
from account.forms import AccountAuthenticationForm,RegisterUserForm

@pytest.mark.django_db
def test_yes_register_user_form():
    data = {
        'email':'testuser@gmail.com',
        'username':'testuser',
        'password1':'Xqjrqp8800',
        'password2':'Xqjrqp8800'
    }
    form = RegisterUserForm(data)
    assert form.is_valid() == True

@pytest.mark.django_db
def test_mail_already_in_use_register_user_form():
    user = Account.objects.create(
        email="testuser@gmail.com",
        username="testuser2",
    )
    data = {
        'email':'testuser@gmail.com',
        'username':'testuser',
        'password1':'Xqjrqp8800',
        'password2':'Xqjrqp8800'
    }
    form = RegisterUserForm(data)
    assert form.is_valid() == False
    
@pytest.mark.django_db
def test_username_already_in_use_register_user_form():
    user = Account.objects.create(
        email="testuser@gmail.com",
        username="testuser2",
    )
    data = {
        'email':'testuser2@gmail.com',
        'username':'testuser2',
        'password1':'Xqjrqp8800',
        'password2':'Xqjrqp8800'
    }
    form = RegisterUserForm(data)
    assert form.is_valid() == False
    
@pytest.mark.django_db
def test_wrong_credentials_account_auth_user_form():
    user = Account.objects.create(
        username='testuser',
        email='testuser@gmail.com',
    )
    data = {
        'email':'testuser@gmail.com',
        'password':'Xqjrqp8800'
    }
    form = AccountAuthenticationForm(data)
    assert form.is_valid() == False

@pytest.mark.django_db
def test_no_user_account_auth_user_form():
    data = {
        'email':'testuser@gmail.com',
        'password':'Xqjrqp8800'
    }
    form = AccountAuthenticationForm(data)
    assert form.is_valid() == False   
