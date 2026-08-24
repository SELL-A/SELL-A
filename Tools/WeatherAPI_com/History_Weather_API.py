import os
import requests

def History_Weather_API(city, language, dt, end_dt):
    """
    :API_description: Retrieve historical weather data for a specific date and location, starting from January 1, 2010.
    Today is 2026-06-19.
    :param city: The location for which the weather history is requested.
    :param language: The language in which the weather data should be returned(e.g., "en").
    :param dt:For history API 'dt' should be on or after 1st Jan, 2010 in yyyy-MM-dd format.
    :param end_dt:For history API 'end_dt' should be on or before the current date in yyyy-MM-dd format. Restrict date output for History API method. Should be on or after 1st Jan, 2010. Make sure end_dt is equal to or greater than 'dt'.
    :response_schema: 
    ```json
{
  "location": {
    "name": "London",
    "region": "City of London, Greater London",
    "country": "United Kingdom",
    "lat": 51.5171,
    "lon": -0.1062,
    "tz_id": "Europe/London",
    "localtime_epoch": 1781883933,
    "localtime": "2026-06-19 16:45"
  },
  "forecast": {
    "forecastday": [
      {
        "date": "2026-06-05",
        "date_epoch": 1780617600,
        "day": {
          "maxtemp_c": 17.9,
          "maxtemp_f": 64.3,
          "mintemp_c": 10.3,
          "mintemp_f": 50.5,
          "avgtemp_c": 14,
          "avgtemp_f": 57.1,
          "maxwind_mph": 11.2,
          "maxwind_kph": 18,
          "totalprecip_mm": 0.3,
          "totalprecip_in": 0.01,
          "totalsnow_cm": 0,
          "avgvis_km": 10,
          "avgvis_miles": 6,
          "avghumidity": 66,
          "daily_will_it_rain": 1,
          "daily_chance_of_rain": 100,
          "daily_will_it_snow": 0,
          "daily_chance_of_snow": 0,
          "condition": {
            "text": "Patchy rain possible",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
            "code": 1063
          },
          "uv": 4.8
        },
        "astro": {
          "sunrise": "04:45 AM",
          "sunset": "09:11 PM",
          "moonrise": "12:43 AM",
          "moonset": "09:27 AM",
          "moon_phase": "Last Quarter",
          "moon_illumination": 64
        },
        "hour": [
          {
            "time_epoch": 1780614000,
            "time": "2026-06-05 00:00",
            "temp_c": 12.2,
            "temp_f": 54,
            "is_day": 0,
            "condition": {
              "text": "Partly cloudy",
              "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
              "code": 1003
            },
            "wind_mph": 10.5,
            "wind_kph": 16.9,
            "wind_degree": 251,
            "wind_dir": "WSW",
            "pressure_mb": 1005,
            "pressure_in": 29.68,
            "precip_mm": 0,
            "precip_in": 0,
            "snow_cm": 0,
            "humidity": 85,
            "cloud": 54,
            "feelslike_c": 10.5,
            "feelslike_f": 50.9,
            "windchill_c": 10.5,
            "windchill_f": 50.9,
            "heatindex_c": 12.2,
            "heatindex_f": 54,
            "dewpoint_c": 9.8,
            "dewpoint_f": 49.6,
            "will_it_rain": 0,
            "chance_of_rain": 0,
            "will_it_snow": 0,
            "chance_of_snow": 0,
            "vis_km": 10,
            "vis_miles": 6,
            "gust_mph": 15.9,
            "gust_kph": 25.7,
            "uv": 0
          },
          {
            "time_epoch": 1780617600,
            "time": "2026-06-05 01:00",
            "temp_c": 11.8,
            "temp_f": 53.3,
            "is_day": 0,
            "condition": {
              "text": "Partly cloudy",
              "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
              "code": 1003
            },
            "wind_mph": 10.3,
            "wind_kph": 16.6,
            "wind_degree": 251,
            "wind_dir": "WSW",
            "pressure_mb": 1006,
            "pressure_in": 29.7,
            "precip_mm": 0,
            "precip_in": 0,
            "snow_cm": 0,
            "humidity": 86,
            "cloud": 60,
            "feelslike_c": 10,
            "feelslike_f": 50,
            "windchill_c": 10,
            "windchill_f": 50,
            "heatindex_c": 11.8,
            "heatindex_f": 53.3,
            "dewpoint_c": 9.6,
            "dewpoint_f": 49.2,
            "will_it_rain": 0,
            "chance_of_rain": 0,
            "will_it_snow": 0,
            "chance_of_snow": 0,
            "vis_km": 10,
            "vis_miles": 6,
            "gust_mph": 15.5,
            "gust_kph": 25,
            "uv": 0
          }
        ]
      }
    ]
  }
}
    ```
    """
    url = "https://weatherapi-com.p.rapidapi.com/history.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"q": city, "lang": language, "dt": dt, "end_dt": end_dt}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

