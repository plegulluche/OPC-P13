import pytest
from account.models import Account
from event.models import Category, City, Customer, Evenement


@pytest.mark.django_db
def test_category_model():

    new_category = Category.objects.create(title="Titre")

    expected_value = "Titre"
    assert str(new_category.title) == expected_value
    assert new_category.__str__() == new_category.title


@pytest.mark.django_db
def test_city_model():

    new_city = City.objects.create(
        name="paris", zipcode="75000", latitude=12.254, longitude=12.654, insee="12345"
    )

    expected_value = "paris"
    assert str(new_city.name) == expected_value
    assert new_city.__str__() == new_city.name


@pytest.mark.django_db
def test_customer_model():
    city = City.objects.create(name="paris", zipcode="75", insee="75000")
    user = Account.objects.create(email="blob@gmail.com", username="blob")
    new_customer = Customer.objects.create(
        firstname="bob",
        lastname="leponge",
        phone="0652458798",
        company="",
        street_number="12345",
        streetname="streetname",
        city=city,
        user=user,
    )

    expected_value = "bob"
    assert str(new_customer.firstname) == expected_value
    assert new_customer.__str__() == "leponge bob"


@pytest.mark.django_db
def test_customer_with_company_model():
    city = City.objects.create(name="paris", zipcode="75", insee="75000")
    user = Account.objects.create(email="blob@gmail.com", username="blob")
    new_customer = Customer.objects.create(
        firstname="bob",
        lastname="leponge",
        phone="0652458798",
        company="test",
        street_number="12345",
        streetname="streetname",
        city=city,
        user=user,
    )

    expected_value = "bob"
    assert str(new_customer.firstname) == expected_value
    assert new_customer.__str__() == "test"


@pytest.mark.django_db
def test_evenement_model():
    user = Account.objects.create(email="blob@gmail.com", username="blob")
    city = City.objects.create(name="paris", zipcode="75", insee="75000")
    customer = Customer.objects.create(
        phone="06666666", street_number="75", streetname="rue", user=user, city=city
    )
    category = Category.objects.create(title="cate")

    new_evenement = Evenement.objects.create(
        title="event test",
        event_start="2022-03-05 01:00:00+01",
        event_end="2022-03-05 01:00:00+01",
        all_day=False,
        description="description",
        category=category,
        user=user,
        customer=customer,
    )

    expected_value = "event test"
    assert str(new_evenement.title) == expected_value
    assert new_evenement.__str__() == "event test"
