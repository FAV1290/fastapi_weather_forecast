import geopy.geocoders
import geopy.location


from constants import GEOCODER_USER_AGENT


def fetch_geocoder_location_object(location_input: str) -> geopy.location.Location | None:
    geolocator = geopy.geocoders.Nominatim(user_agent=GEOCODER_USER_AGENT)
    target_location = geolocator.geocode(location_input, language='en')
    return target_location
