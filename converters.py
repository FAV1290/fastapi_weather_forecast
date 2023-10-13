import geopy.geocoders
import geopy.location


from open_weather_api import OpenWeatherAPI


def convert_str_to_location(location_input: str) -> geopy.location.Location | None:
    geolocator = geopy.geocoders.Nominatim(user_agent='dummy_fastapi_weather_app')
    target_location = geolocator.geocode(location_input, language='en')
    return target_location


def prepare_app_response_json(location: geopy.location.Location) -> dict[str, str | float]:
    weather = OpenWeatherAPI()
    current_temperature = weather.parse_current_temperature(location.latitude, location.longitude)
    response_json = {
        'location address' : location.address,
        'location name' : location.raw['name'],
        'latitude' : location.latitude,
        'longitude' : location.longitude,
        'current temperature' : current_temperature,
    }
    return response_json
