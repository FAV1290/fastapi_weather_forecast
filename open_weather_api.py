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

    def parse_current_weather(
        self,
        latitude: float,
        longitude: float,
    ) -> requests.Response | None:
        api_call_params: dict[str, float | str] = {
            'lat' : latitude,
            'lon' : longitude,
            'appid' : self.api_key,
            'units' : self.units,
        }
        response = requests.get(self.url, params=api_call_params)
        if response.status_code == 200:
            return response
        return None
    
    def parse_current_temperature(
        self,
        latitude: float,
        longitude: float,
    ) -> float | None:
        response = self.parse_current_weather(latitude, longitude)
        if response is None:
            return None
        return response.json()['main']['temp']
   