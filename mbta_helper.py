import json
import os
import pprint
import urllib.request
import certifi

from dotenv import load_dotenv

import mbta_helper

# Load environment variables
load_dotenv()

print(mbta_helper.find_nearest_mbta_stop("Boston Common"))

# Get API keys from environment variables
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# Useful base URLs (you need to add the appropriate parameters for each API request)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

def get_coordinates(address):
    query = urllib.parse.quote(address)
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        coordinates = data["features"][0]["geometry"]["coordinates"]
        return coordinates[1], coordinates[0]  # lat, lon


def get_nearest_stop(lat, lon):
    url = f"{MBTA_BASE_URL}?sort=distance&filter[latitude]={lat}&filter[longitude]={lon}&api_key={MBTA_API_KEY}"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        stop = data["data"][0]
        stop_name = stop["attributes"]["name"]
        wheelchair_accessible = stop["attributes"]["wheelchair_boarding"] == 1
        return stop_name, wheelchair_accessible


def find_nearest_mbta_stop(address):
    """"""
    lat, lon = get_coordinates(address)
    return get_nearest_stop(lat, lon)


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    pass


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    pass


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    pass


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You should test all the above functions here
    """
    query = "Boston Common"
    query = query.replace(
        " ", "%20"
    )  # In URL encoding, spaces are typically replaced with "%20". You can also use `urllib.parse.quote` function.

    # lat, lng = get_coordinates(query)
    # # print(lat, lng)
    # stop_info = get_nearest_stop(lat, lng)
    # print(stop_info)
    print(find_nearest_mbta_stop(query))


if __name__ == "__main__":
    main()
