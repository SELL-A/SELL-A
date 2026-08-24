import os
import requests

def Realtime_Weather_API(location):
    """
    :API_description: Provides real-time weather data for a specified location, including temperature, wind speed, and humidity, with both metric and imperial units.
    :param location: The location for which to retrieve weather data, specified as a latitude and longitude string (e.g., "53.1,-0.13",city name,) .
    :response_schema: 
    ```json
{
  "location": {
    "name": "Moor Side",
    "region": "Lincolnshire",
    "country": "United Kingdom",
    "lat": 53.1,
    "lon": -0.142,
    "tz_id": "Europe/London",
    "localtime_epoch": 1781885124,
    "localtime": "2026-06-19 17:05"
  },
  "current": {
    "last_updated_epoch": 1781883900,
    "last_updated": "2026-06-19 16:45",
    "temp_c": 29.1,
    "temp_f": 84.4,
    "is_day": 1,
    "condition": {
      "text": "Partly Cloudy",
      "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
      "code": 1003
    },
    "wind_mph": 15.7,
    "wind_kph": 25.2,
    "wind_degree": 215,
    "wind_dir": "SW",
    "pressure_mb": 1009,
    "pressure_in": 29.8,
    "precip_mm": 0,
    "precip_in": 0,
    "humidity": 37,
    "cloud": 25,
    "feelslike_c": 31,
    "feelslike_f": 87.7,
    "windchill_c": 25.9,
    "windchill_f": 78.6,
    "heatindex_c": 26.9,
    "heatindex_f": 80.4,
    "dewpoint_c": 16.5,
    "dewpoint_f": 61.8,
    "vis_km": 10,
    "vis_miles": 6,
    "uv": 4.3,
    "gust_mph": 19.6,
    "gust_kph": 31.5,
    "will_it_rain": 0,
    "chance_of_rain": 4,
    "will_it_snow": 0,
    "chance_of_snow": 0,
    "short_rad": 815.42,
    "diff_rad": 90.43,
    "dni": 1100,
    "gti": 635.32
  }
}
    ```
    """
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"q": location}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
