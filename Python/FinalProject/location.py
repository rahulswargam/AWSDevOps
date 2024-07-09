# location.py

import sys
from geopy.geocoders import Nominatim

def get_location_info(location_name):
    try:
        geolocator = Nominatim(user_agent="location_script")
        location = geolocator.geocode(location_name)
        if location:
            print(f"Location: {location.address}")
            print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
        else:
            print(f"Location '{location_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python location.py <location>")
        sys.exit(1)

    location_name = ' '.join(sys.argv[1:])
    get_location_info(location_name)