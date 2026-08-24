import os
import requests

def Nearby_Stations(lat, lon):
    """
    :API_description: Retrieve a list of nearby weather stations based on geographical coordinates.
    :param lat: Latitude of the location.
    :param lon: Longitude of the location.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "meta": {
      "type": "object",
      "properties": {
        "generated": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp indicating when the data was generated."
        }
      },
      "required": ["generated"]
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the location."
          },
          "name": {
            "type": "object",
            "properties": {
              "en": {
                "type": "string",
                "description": "Name of the location in English."
              }
            },
            "required": ["en"]
          },
          "distance": {
            "type": "number",
            "description": "Distance from a reference point to the location."
          }
        },
        "required": ["id", "name", "distance"]
      }
    }
  },
  "required": ["meta", "data"]
}
```
    """
    url = "https://meteostat.p.rapidapi.com/stations/nearby"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"lat": lat, "lon": lon}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "meteostat.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

