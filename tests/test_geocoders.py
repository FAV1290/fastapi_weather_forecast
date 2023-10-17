from geocoders import fetch_geocoder_location_object


def test_fetch_geocoder_location_object() -> None:
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
        location = fetch_geocoder_location_object(location_name)
        if location is None:
            assert expected_coordinates is None
        else: 
            assert location.latitude, location.longitude == expected_coordinates
