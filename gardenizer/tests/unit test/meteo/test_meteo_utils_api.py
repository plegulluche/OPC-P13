import pytest
import json
from meteo.utils.api import Weathermanager
from meteo.models import MeteoData


def mock_requestget(*args, **kwargs):
    """Mock the requests module to get a data structure and content for tests"""
    datastructure = {
        "city": {
            "insee": "35238",
            "cp": 35000,
            "name": "Rennes",
            "latitude": 48.112,
            "longitude": -1.6819,
            "altitude": 38
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
                "gustx": 45
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
                "gustx": 38
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
                "gustx": 29
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
                "gustx": 30
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
                "gustx": 30
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
                "gustx": 27
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
                "gustx": 23
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
                "gustx": 31
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
                "gustx": 38
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
                "gustx": 39
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
                "gustx": 39
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
                "gustx": 39
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
                "gustx": 48
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
                "gustx": 47
            }
        ]
    }
    
    class mock_response:
        def __init__(self,data):
            self.data = json.dumps(data)
            self.status_code = self.status()
            
        def status(self):
            return 200
        
        def json(self):
            return json.loads(self.data)

    response = mock_response(datastructure)
    return response

@pytest.mark.django_db
def test_response_status_is_200(mocker):
    """test if get_weekly forecast method create meteo objects in database"""
    
    mocker.patch("requests.get", mock_requestget)
    api_caller = Weathermanager()
    result = api_caller.get_weekly_forecast(35238)
    meteo = MeteoData.objects.all()
    assert meteo is not None