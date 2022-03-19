import pytest

from meteo.models import MeteoData


@pytest.mark.django_db
def test_meteo_model():

    new_meteo = MeteoData.objects.create(
        day=1,
        weather=24,
        tmin=1,
        tmax=2,
        probarain=1,
        probafrost=2,
        probawind=2,
        insee="12345",
        datetime='2022-03-05 01:00:00+01'
    )

    expected_value = "12345"
    assert str(new_meteo.insee) == expected_value

    assert new_meteo.__str__() == new_meteo.insee