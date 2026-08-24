import os
import requests

def IsOnWater(lat, lon):
    """
    :API_description: Determines if a given GPS coordinate is on water, specifying whether it's a sea or a lake.
    :param lat: Latitude of the location to check.
    :param lon: Longitude of the location to check.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "isOnWater": {
      "type": "boolean",
      "description": "Indicates whether the location is on water."
    },
    "sea": {
      "type": "boolean",
      "description": "Indicates whether the water body is a sea."
    },
    "lake": {
      "type": "boolean",
      "description": "Indicates whether the water body is a lake."
    }
  },
  "required": ["isOnWater", "sea", "lake"]
}
```
    """
    url = "https://geocodeapi.p.rapidapi.com/isonwater"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"lat": lat, "lon": lon}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "geocodeapi.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")