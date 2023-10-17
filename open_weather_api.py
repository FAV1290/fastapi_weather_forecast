import requests


from constants import API_CALL_URL, API_KEY


class OpenWeatherAPI:
    def __init__(
        self,
        api_call_url: str = API_CALL_URL,
        api_key: str = API_KEY,
        units: str = 'metric'
    ):
        self.url = api_call_url
        self.api_key = api_key
        self.units = units

    def fetch_api_weather_response(self, latitude: float, longitude: float) -> requests.Response:
        api_call_params: dict[str, float | str] = {
            'lat': latitude,
            'lon': longitude,
            'appid': self.api_key,
            'units': self.units,
        }
        return requests.get(self.url, params=api_call_params)    
    
    def parse_current_temperature(
        self,
        latitude: float,
        longitude: float,
    ) -> float | None:
        response = self.fetch_api_weather_response(latitude, longitude)
        if response.status_code == 200:
            return response.json()['main']['temp']
        return None
