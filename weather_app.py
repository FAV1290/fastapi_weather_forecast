import fastapi


from converters import convert_str_to_location, prepare_app_response_json


app = fastapi.FastAPI()


@app.get('/weather')
def read_no_location_input() -> dict[str, str]:
    return {'error' : 'please add / and location name in adress'}


@app.get('/weather/{location_input}')
def read_weather(location_input: str) -> dict[str, str | float]:
    location = convert_str_to_location(location_input)
    if location is None:
        return {'error' : 'incorrect location name'}
    response = prepare_app_response_json(location)
    return response
