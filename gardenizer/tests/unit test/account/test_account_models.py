import pytest

from account.models import Account


@pytest.mark.django_db
def test_Account_user_model():

    new_user = Account.objects.create(
        username="blob", email="blob@blobmail.com", password="SuperPass1234"
    )

    expected_value = "blob@blobmail.com"
    assert str(new_user.email) == expected_value

    assert new_user.__str__() == new_user.email
