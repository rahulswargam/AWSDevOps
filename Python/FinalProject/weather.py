# weather.py

import sys
import requests

def get_weather(api_key, city_id):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_info = data["main"]
            weather_info["wind_speed"] = data["wind"]["speed"]
            weather_info["cloudiness"] = data["clouds"]["all"]
            sys.stdout.write("Weather Information:\n")
            sys.stdout.write(f"Temperature: {weather_info['temp']}°C\n")
            sys.stdout.write(f"Min Temperature: {weather_info['temp_min']}°C\n")
            sys.stdout.write(f"Max Temperature: {weather_info['temp_max']}°C\n")
            sys.stdout.write(f"Humidity: {weather_info['humidity']}%\n")
            sys.stdout.write(f"Wind Speed: {weather_info['wind_speed']} m/s\n")
            sys.stdout.write(f"Cloudiness: {weather_info['cloudiness']}%\n")
            sys.stdout.write(f"Pressure: {weather_info['pressure']} hPa\n")
        else:
            sys.stderr.write(f"Error: {data['message']}\n")
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python weather.py <api_key> <city_id>")
        sys.exit(1)

    api_key = sys.argv[1]
    city_id = sys.argv[2]
    get_weather(api_key, city_id)
