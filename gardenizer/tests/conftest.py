from calendar import c
import pytest
from event.models import Category,Customer,City,Evenement
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
    email = "foo2@gmail.com"
    password = "oAy&mX57qeo&C3cE"
    username = "Donald2duck"
    new_user = Account()
    new_user.username = username
    new_user.email = email
    new_user.password = password
    new_user.save()
    new_user.set_password(password)
    new_user.save()
    return new_user

@pytest.fixture
def create_city():
    """create a city object for tests"""
    new_city = City.objects.create(
        name='testcity',
        zipcode='75000',
        insee='75000'
    )
    return new_city
    

@pytest.fixture
def create_categories():
    """create category objects for tests"""
    categories = ["Entretient et révision matériel", "Chantier"]
    for category in categories:
        obj, created = Category.objects.get_or_create(
            title = f'{category}'
        )
        
@pytest.fixture
def create_customer(create_city,create_new_user):
    """create customer object for test"""
    new_customer = Customer.objects.create(
        firstname = "bob",
        lastname = "l'eponge",
        phone = '0666666666',
        company = '',
        street_number = "25bis",
        streetname = 'courant du coquillage',
        city=create_city,
        user=create_new_user
        
    )
    return new_customer


@pytest.fixture
def create_maintenance_event(create_new_user,create_customer):
    """create a maintenance event for tests"""
    category = Category.objects.create(title="Entretient et révision matériel")
    new_event = Evenement.objects.create(
        title = 'a title',
        event_start = '2022-03-09T10:45',
        event_end = '2022-03-09T09:45',
        description = 'a description',
        category = category,
        customer = create_customer,
        user = create_new_user
    )


@pytest.fixture
def create_customer_event(create_new_user,create_customer):
    """create a customer event for tests"""
    category = Category.objects.create(title='Chantier')
    new_event = Evenement.objects.create(
        title = 'a title',
        event_start = '2022-03-09T10:45',
        event_end = '2022-03-09T09:45',
        description = 'a description',
        category = category,
        customer = create_customer,
        user = create_new_user
    )


@pytest.fixture
def yes_add_maintenance_event_form_data():
    """gives valid data for a test"""
    return {
        'title':'event test',
        'description':'a short description',
        'event_start':'2022-03-09T10:45',
        'event_end':'2022-03-09T10:45'
    }
    
@pytest.fixture
def no_add_maintenance_event_form_data():
    """gives invalid data for a test"""
    return {
        'title':'',
        'description':'',
        'event_start':'',
        'event_end':''
    }
    
@pytest.fixture
def yes_add_customer_event_form_data():
    """gives valid data for a test"""
    return {
        'title':'event test',
        'description':'a short description',
        'event_start':'2022-03-09T10:45',
        'event_end':'2022-03-09T10:45',
        
    }

@pytest.fixture
def no_add_customer_event_form_data():
    """gives invalid data for a test"""
    return {
        'title':'',
        'description':'',
        'event_start':'',
        'event_end':'',
        
    }
    
@pytest.fixture
def yes_add_customer_form_data(create_city):
    """gives valid post data for a test"""
    
    return {
        'firstname':'customer',
        'lastname':'lastname',
        'phone':'066666666',
        'company':'fakecompany',
        'street_number':'125',
        'streetname':'une rue',
        'city':create_city.id,
    }
    
@pytest.fixture
def no_add_customer_form_data(create_city):
    """gives invalid post data for a test"""
    return {
        'firstname':'test customer',
        'lastname':'lastname',
        'phone':'',
        'company':'',
        'street_number':'',
        'streetname':'une rue',
        'city':create_city.id
    }