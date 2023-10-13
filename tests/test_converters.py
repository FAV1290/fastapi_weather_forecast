import time


from open_weather_api import OpenWeatherAPI
from converters import convert_str_to_location, prepare_app_response_json


def test_fetch_location_coordinates() -> None:
    city_name_to_coordinates_map = {
        'yerevan' : (40.1777112, 44.5126233),
        'moscow' : (55.625578, 37.6063916),
        'paris' : (48.8534951, 2.3483915),
        'berlin' : (52.5170365, 13.3888599),
        'new_york' : (40.7127281, -74.0060152),
        'gumri' : (40.7852085, 43.8416095),
        'adadadafeogfekfeolwkfd' : None,
        '1111111111111' : None,
        '' : None,
        'dilidgan' : None,
        'armenia_dilijan' : (40.7417183, 44.8721946),
    }
    for location_name, expected_coordinates in city_name_to_coordinates_map.items():
        location = convert_str_to_location(location_name)
        if location is None:
            assert expected_coordinates is None
        else: 
            assert location.latitude, location.longitude == expected_coordinates


def test_prepare_app_response_json() -> None:
    city_name_to_coordinates_map = {
        'Yerevan, Armenia' : (40.1777112, 44.5126233),
        'Moscow, Central Federal District, Russia' : (55.625578, 37.6063916),
        'Berlin, Germany' : (52.5170365, 13.3888599),
        'New York, United States' : (40.7127281, -74.0060152),
        'Gyumri, Akhuryan region, Shirak Province, Armenia' : (40.7852085, 43.8416095),
        'Dilijan, Dilijan Region, Tavush Province, Armenia' : (40.7417183, 44.8721946),
    }
    for location_address, expected_coordinates in city_name_to_coordinates_map.items():
        weather = OpenWeatherAPI()
        location = convert_str_to_location(location_address)
        response_json = prepare_app_response_json(location)
        temperature = response_json['current temperature']
        expected_temperature = weather.parse_current_temperature(*expected_coordinates)
        assert response_json['latitude'], response_json['longitude'] == expected_coordinates 
        assert response_json['location address'] == location_address
        assert abs(temperature - expected_temperature) <= 0.1
