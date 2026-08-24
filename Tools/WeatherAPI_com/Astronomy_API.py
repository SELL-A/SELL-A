import os
import requests

def Astronomy_API(location):
    """
    :API_description: Retrieve real-time astronomical data including sunrise, sunset, moonrise, moonset, moon phase, and illumination for a specified location.
    :param location: The location for which to retrieve astronomy data (e.g., city name or coordinates).
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
    "localtime_epoch": 1781884066,
    "localtime": "2026-06-19 16:47"
  },
  "astronomy": {
    "astro": {
      "sunrise": "04:42 AM",
      "sunset": "09:20 PM",
      "moonrise": "08:07 AM",
      "moonset": "Does not set today",
      "moon_phase": "Waxing Crescent",
      "moon_illumination": 12,
      "is_moon_up": 0,
      "is_sun_up": 0
    }
  }
}
    ```
    """
    url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"
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