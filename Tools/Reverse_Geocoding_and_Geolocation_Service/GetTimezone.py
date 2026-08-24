import os
import requests

def GetTimezone(latitude, longitude):
    """
    :API_description: Retrieves detailed timezone information for a given geo-location, including timezone name, ID, and current local time.
    :param latitude: The latitude of the location.
    :param longitude: The longitude of the location.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "TimeZoneId": {
      "type": "string",
      "description": "The identifier for the time zone, e.g., 'America/New_York'."
    },
    "GMT_offset": {
      "type": "integer",
      "description": "The offset from Greenwich Mean Time (GMT) in hours, e.g., -5."
    },
    "TimeZoneName": {
      "type": "string",
      "description": "The name of the time zone, e.g., 'EDT' (Eastern Daylight Time)."
    },
    "LocalTime_Now": {
      "type": "string",
      "description": "The current local time in the specified time zone, e.g., '5:48:07 PM'."
    },
    "Country": {
      "type": "string",
      "description": "The name of the country associated with the time zone, e.g., 'United States of America'."
    },
    "CountryId": {
      "type": "string",
      "description": "The ISO 3166-1 alpha-2 code for the country, e.g., 'US'."
    }
  },
  "required": ["TimeZoneId", "GMT_offset", "TimeZoneName", "LocalTime_Now", "Country", "CountryId"]
}
```
    """
    url = "https://geocodeapi.p.rapidapi.com/GetTimezone"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"latitude": latitude, "longitude": longitude}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "geocodeapi.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")