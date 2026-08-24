import os
import requests

def GetLargestCities(latitude, longitude, range):
    """
    :API_description: Retrieves detailed information about multiple cities, including names, populations, geographic coordinates, and country details, based on a reference point defined by latitude, longitude, and a radial range.
    :param latitude: The latitude of the location.
    :param longitude: The longitude of the location.
    :param range: The range within which to find the largest cities(e.g. radial lookup range in meters (max 100.000) Default: 50000).
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "City": {
        "type": "string",
        "description": "The name of the city."
      },
      "Population": {
        "type": "integer",
        "description": "The population of the city."
      },
      "Latitude": {
        "type": "number",
        "description": "The latitude coordinate of the city."
      },
      "Longitude": {
        "type": "number",
        "description": "The longitude coordinate of the city."
      },
      "Country": {
        "type": "string",
        "description": "The name of the country where the city is located."
      },
      "CountryId": {
        "type": "string",
        "description": "The ISO 3166-1 alpha-2 country code."
      },
      "TimeZoneId": {
        "type": "string",
        "description": "The IANA time zone identifier."
      },
      "TimeZoneName": {
        "type": "string",
        "description": "The name of the time zone."
      },
      "TimeZone_GMT_offset": {
        "type": "integer",
        "description": "The GMT offset of the time zone in hours."
      },
      "LocalTimeNow": {
        "type": "string",
        "description": "The current local time in the city."
      },
      "Distance": {
        "type": "number",
        "description": "The distance from a reference point to the city."
      },
      "Bearing": {
        "type": "number",
        "description": "The bearing from a reference point to the city in degrees."
      },
      "CompassDirection": {
        "type": "string",
        "description": "The compass direction from a reference point to the city."
      }
    },
    "required": [
      "City",
      "Population",
      "Latitude",
      "Longitude",
      "Country",
      "CountryId",
      "TimeZoneId",
      "TimeZoneName",
      "TimeZone_GMT_offset",
      "LocalTimeNow",
      "Distance",
      "Bearing",
      "CompassDirection"
    ]
  }
}
```
    """
    url = "https://geocodeapi.p.rapidapi.com/GetLargestCities"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"latitude": latitude, "longitude": longitude, "range": range}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "geocodeapi.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")