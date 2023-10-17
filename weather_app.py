import fastapi
import geopy.location


from open_weather_api import OpenWeatherAPI
from geocoders import fetch_geocoder_location_object


app = fastapi.FastAPI()


def prepare_app_response_json(
    location: geopy.location.Location,
    current_temperature: float,
) -> dict[str, str | float]:
    response_json = {
        'location address': location.address,
        'location name': location.raw['name'],
        'latitude': location.latitude,
        'longitude': location.longitude,
        'current temperature': current_temperature,
    }
    return response_json


@app.get('/weather')
def read_no_location_input() -> dict[str, str]:
    return {'error' : 'please add / and location name in adress'}


@app.get('/weather/{location_input}')
def read_weather(location_input: str) -> dict[str, str | float]:
    location = fetch_geocoder_location_object(location_input)
    if location is None:
        return {'error' : 'incorrect location name'}
    weather = OpenWeatherAPI()
    current_temp = weather.parse_current_temperature(location.latitude, location.longitude)
    if current_temp is None:
        return {'error' : 'parsing error'}
    response = prepare_app_response_json(location, current_temp)
    return response
