import pytest
from event.models import Category, Customer, City, Evenement
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
    client.login(email=email, password=password)
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
    new_city = City.objects.create(name="testcity", zipcode="75000", insee="75000")
    return new_city


@pytest.fixture
def create_categories():
    """create category objects for tests"""
    categories = ["Entretient et révision matériel", "Chantier"]
    for category in categories:
        obj, created = Category.objects.get_or_create(title=f"{category}")


@pytest.fixture
def create_customer(create_city, create_new_user):
    """create customer object for test"""
    new_customer = Customer.objects.create(
        firstname="bob",
        lastname="l'eponge",
        phone="0666666666",
        company="",
        street_number="25bis",
        streetname="courant du coquillage",
        city=create_city,
        user=create_new_user,
    )
    return new_customer


@pytest.fixture
def create_maintenance_event(create_new_user, create_customer):
    """create a maintenance event for tests"""
    category = Category.objects.create(title="Entretient et révision matériel")
    Evenement.objects.create(
        title="a title",
        event_start="2022-03-09T10:45",
        event_end="2022-03-09T09:45",
        description="a description",
        category=category,
        customer=create_customer,
        user=create_new_user,
    )


@pytest.fixture
def create_customer_event(create_new_user, create_customer):
    """create a customer event for tests"""
    category = Category.objects.create(title="Chantier")
    Evenement.objects.create(
        title="a title",
        event_start="2022-03-09T10:45",
        event_end="2022-03-09T09:45",
        description="a description",
        category=category,
        customer=create_customer,
        user=create_new_user,
    )


@pytest.fixture
def yes_add_maintenance_event_form_data():
    """gives valid data for a test"""
    return {
        "title": "event test",
        "description": "a short description",
        "event_start": "2022-03-09T10:45",
        "event_end": "2022-03-09T10:45",
    }


@pytest.fixture
def no_add_maintenance_event_form_data():
    """gives invalid data for a test"""
    return {"title": "", "description": "", "event_start": "", "event_end": ""}


@pytest.fixture
def yes_add_customer_event_form_data():
    """gives valid data for a test"""
    return {
        "title": "event test",
        "description": "a short description",
        "event_start": "2022-03-09T10:45",
        "event_end": "2022-03-09T10:45",
    }


@pytest.fixture
def no_add_customer_event_form_data():
    """gives invalid data for a test"""
    return {
        "title": "",
        "description": "",
        "event_start": "",
        "event_end": "",
    }


@pytest.fixture
def yes_add_customer_form_data(create_city):
    """gives valid post data for a test"""

    return {
        "firstname": "customer",
        "lastname": "lastname",
        "phone": "066666666",
        "company": "fakecompany",
        "street_number": "125",
        "streetname": "une rue",
        "city": create_city.id,
    }


@pytest.fixture
def no_add_customer_form_data(create_city):
    """gives invalid post data for a test"""
    return {
        "firstname": "test customer",
        "lastname": "lastname",
        "phone": "",
        "company": "",
        "street_number": "",
        "streetname": "une rue",
        "city": create_city.id,
    }


@pytest.fixture
def fake_api_data():
    return {
        "city": {
            "insee": "35238",
            "cp": 35000,
            "name": "Rennes",
            "latitude": 48.112,
            "longitude": -1.6819,
            "altitude": 38,
        },
        "update": "2022-03-22T11:14:54+01:00",
        "forecast": [
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 0,
                "datetime": "2022-03-22T01:00:00+0100",
                "wind10m": 15,
                "gust10m": 45,
                "dirwind10m": 134,
                "rr10": 0,
                "rr1": 0,
                "probarain": 10,
                "weather": 1,
                "tmin": 7,
                "tmax": 16,
                "sun_hours": 9,
                "etp": 2,
                "probafrost": 0,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 45,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 1,
                "datetime": "2022-03-23T01:00:00+0100",
                "wind10m": 10,
                "gust10m": 38,
                "dirwind10m": 126,
                "rr10": 0,
                "rr1": 0,
                "probarain": 0,
                "weather": 1,
                "tmin": 5,
                "tmax": 16,
                "sun_hours": 11,
                "etp": 2,
                "probafrost": 0,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 38,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 2,
                "datetime": "2022-03-24T01:00:00+0100",
                "wind10m": 15,
                "gust10m": 29,
                "dirwind10m": 88,
                "rr10": 0,
                "rr1": 0,
                "probarain": 0,
                "weather": 1,
                "tmin": 5,
                "tmax": 17,
                "sun_hours": 10,
                "etp": 2,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 29,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 3,
                "datetime": "2022-03-25T01:00:00+0100",
                "wind10m": 15,
                "gust10m": 30,
                "dirwind10m": 65,
                "rr10": 0,
                "rr1": 0,
                "probarain": 0,
                "weather": 0,
                "tmin": 5,
                "tmax": 16,
                "sun_hours": 12,
                "etp": 2,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 30,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 4,
                "datetime": "2022-03-26T01:00:00+0100",
                "wind10m": 20,
                "gust10m": 30,
                "dirwind10m": 56,
                "rr10": 0,
                "rr1": 0,
                "probarain": 20,
                "weather": 1,
                "tmin": 5,
                "tmax": 16,
                "sun_hours": 11,
                "etp": 3,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 30,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 5,
                "datetime": "2022-03-27T01:00:00+0100",
                "wind10m": 15,
                "gust10m": 27,
                "dirwind10m": 65,
                "rr10": 0,
                "rr1": 0,
                "probarain": 40,
                "weather": 3,
                "tmin": 5,
                "tmax": 16,
                "sun_hours": 10,
                "etp": 3,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 27,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 6,
                "datetime": "2022-03-28T02:00:00+0200",
                "wind10m": 10,
                "gust10m": 23,
                "dirwind10m": 79,
                "rr10": 0.2,
                "rr1": 0.2,
                "probarain": 60,
                "weather": 3,
                "tmin": 6,
                "tmax": 16,
                "sun_hours": 7,
                "etp": 2,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 23,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 7,
                "datetime": "2022-03-29T02:00:00+0200",
                "wind10m": 10,
                "gust10m": 23,
                "dirwind10m": 92,
                "rr10": 2.2,
                "rr1": 4.2,
                "probarain": 60,
                "weather": 40,
                "tmin": 6,
                "tmax": 14,
                "sun_hours": 5,
                "etp": 2,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 31,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 8,
                "datetime": "2022-03-30T02:00:00+0200",
                "wind10m": 15,
                "gust10m": 24,
                "dirwind10m": 346,
                "rr10": 3,
                "rr1": 5,
                "probarain": 60,
                "weather": 41,
                "tmin": 6,
                "tmax": 12,
                "sun_hours": 5,
                "etp": 2,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 0,
                "probawind100": 0,
                "gustx": 38,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 9,
                "datetime": "2022-03-31T02:00:00+0200",
                "wind10m": 15,
                "gust10m": 25,
                "dirwind10m": 321,
                "rr10": 4.6,
                "rr1": 8.4,
                "probarain": 60,
                "weather": 41,
                "tmin": 4,
                "tmax": 11,
                "sun_hours": 5,
                "etp": 2,
                "probafrost": 30,
                "probafog": 0,
                "probawind70": 10,
                "probawind100": 0,
                "gustx": 39,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 10,
                "datetime": "2022-04-01T02:00:00+0200",
                "wind10m": 15,
                "gust10m": 25,
                "dirwind10m": 227,
                "rr10": 5.6,
                "rr1": 9.4,
                "probarain": 60,
                "weather": 40,
                "tmin": 4,
                "tmax": 11,
                "sun_hours": 5,
                "etp": 2,
                "probafrost": 30,
                "probafog": 0,
                "probawind70": 10,
                "probawind100": 0,
                "gustx": 39,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 11,
                "datetime": "2022-04-02T02:00:00+0200",
                "wind10m": 15,
                "gust10m": 29,
                "dirwind10m": 212,
                "rr10": 7.5,
                "rr1": 9.5,
                "probarain": 60,
                "weather": 40,
                "tmin": 5,
                "tmax": 12,
                "sun_hours": 5,
                "etp": 2,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 10,
                "probawind100": 0,
                "gustx": 39,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 12,
                "datetime": "2022-04-03T02:00:00+0200",
                "wind10m": 20,
                "gust10m": 33,
                "dirwind10m": 218,
                "rr10": 8,
                "rr1": 19,
                "probarain": 60,
                "weather": 41,
                "tmin": 7,
                "tmax": 12,
                "sun_hours": 4,
                "etp": 2,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 10,
                "probawind100": 0,
                "gustx": 48,
            },
            {
                "insee": "35238",
                "cp": 35000,
                "latitude": 48.112,
                "longitude": -1.6819,
                "day": 13,
                "datetime": "2022-04-04T02:00:00+0200",
                "wind10m": 20,
                "gust10m": 32,
                "dirwind10m": 225,
                "rr10": 7.5,
                "rr1": 14.5,
                "probarain": 60,
                "weather": 41,
                "tmin": 7,
                "tmax": 13,
                "sun_hours": 5,
                "etp": 2,
                "probafrost": 10,
                "probafog": 0,
                "probawind70": 10,
                "probawind100": 0,
                "gustx": 47,
            },
        ],
    }
