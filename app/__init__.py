import fastapi


from app.open_weather_api import OpenWeatherAPI
from app.response_creator import prepare_app_response_json
from app.geocoders import fetch_geocoder_location_object


app = fastapi.FastAPI()


@app.get('/weather')
def read_no_location_input() -> dict[str, str]:
    return {'error': 'please add / and location name in address'}


@app.get('/weather/{location_input}')
def read_weather(location_input: str) -> dict[str, str | float]:
    location = fetch_geocoder_location_object(location_input)
    if not location:
        return {'error': 'incorrect location name'}
    weather = OpenWeatherAPI()
    current_temp = weather.parse_current_temperature(location.latitude, location.longitude)
    if not current_temp:
        return {'error': 'parsing error'}
    return prepare_app_response_json(location, current_temp)
