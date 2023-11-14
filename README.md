
<div align='center'><h1>FastAPI Weather report</h1></div>
<p align='center'><img src='readme_assets\img.png' height='256'/></p>


## What is that?
Current temperature in chosen location parser on FastAPI: 
+ Parses current temperature by location name
+ Gets location coordinates via Nominatim geocoder
+ Gets weather info from https://openweathermap.org/

## Requirements
<a href='requirements.txt'>Here they are...</a>

## Project setup
+ Clone repo: `https://github.com/FAV1290/fastapi_weather_forecast`
+ Open repo catalog and install requirements: `pip install -r requirements.txt`
+ Get your free API key on https://openweathermap.org/api
+ Add environment variable or .env line `OPEN_WEATHER_API_KEY` with your API key
+ Start uvicorn server: `python __main__.py`
+ Input `http://127.0.0.1:8000/weather/{location}` (where {location} is your preferred location) in your web browser or...
+ Inpit `http://127.0.0.1:8000/docs`in your web browser and use FastAPI interface to get response

## How does it look?
<img src='readme_assets\screenshot1.png'/>
<img src='readme_assets\screenshot2.png'/>
<img src='readme_assets\screenshot3.png'/>
