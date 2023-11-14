from geopy.location import Location


def prepare_app_response_json(location: Location, current_temp: float) -> dict[str, str | float]:
    response_json = {
        'location address': location.address,
        'location name': location.raw['name'],
        'latitude': location.latitude,
        'longitude': location.longitude,
        'current temperature': current_temp,
    }
    return response_json
