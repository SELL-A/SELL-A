import os
import requests

def GetDistance(lat1, lon1, lat2, lon2):
    """
    :API_description: Calculates the distance between two geographical points using latitude and longitude, providing the distance in meters, kilometers, and miles, along with compass direction and bearing.
    :param lat1: Latitude of the first point.
    :param lon1: Longitude of the first point.
    :param lat2: Latitude of the second point.
    :param lon2: Longitude of the second point.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "CountryStart": {
      "type": "string",
      "description": "The name of the starting country."
    },
    "CountryStartId": {
      "type": "string",
      "description": "The ISO 3166-1 alpha-3 code of the starting country."
    },
    "CountryDestination": {
      "type": "string",
      "description": "The name of the destination country."
    },
    "CountryDestinationId": {
      "type": "string",
      "description": "The ISO 3166-1 alpha-3 code of the destination country."
    },
    "Distance": {
      "type": "number",
      "description": "The distance between the two countries in meters."
    },
    "DistanceInKm": {
      "type": "number",
      "description": "The distance between the two countries in kilometers."
    },
    "DistanceInMiles": {
      "type": "number",
      "description": "The distance between the two countries in miles."
    },
    "Bearing": {
      "type": "number",
      "description": "The bearing angle in degrees from the starting country to the destination country."
    },
    "CompassDirection": {
      "type": "string",
      "description": "The compass direction from the starting country to the destination country."
    }
  },
  "required": [
    "CountryStart",
    "CountryStartId",
    "CountryDestination",
    "CountryDestinationId",
    "Distance",
    "DistanceInKm",
    "DistanceInMiles",
    "Bearing",
    "CompassDirection"
  ]
}
```
    """
    url = "https://geocodeapi.p.rapidapi.com/GetDistance"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"lat1": lat1, "lon1": lon1, "lat2": lat2, "lon2": lon2}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "geocodeapi.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

