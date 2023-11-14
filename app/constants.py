import os
import dotenv


dotenv.load_dotenv()


API_CALL_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = os.environ['OPEN_WEATHER_API_KEY']
GEOCODER_USER_AGENT = 'dummy_fastapi_weather_app'
