import os
import requests

def find_location(q, limit):
    """
    :API_description: Retrieve geographical information about locations matching a specific name, including latitude, longitude, country code, and optional state details.
    :param q: The name of the location to search for.
    :param limit: The maximum number of results to return.
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "lat": {
        "type": "number",
        "description": "Latitude of the location"
      },
      "lon": {
        "type": "number",
        "description": "Longitude of the location"
      },
      "country": {
        "type": "string",
        "description": "Country code of the location"
      },
      "local_names": {
        "type": "object",
        "description": "Local names of the location in various languages",
        "additionalProperties": {
          "type": "string"
        }
      },
      "name": {
        "type": "string",
        "description": "Name of the location"
      },
      "state": {
        "type": "string",
        "description": "State or region of the location (optional)"
      }
    },
    "required": ["lat", "lon", "country", "name"]
  }
}
```
    """
    url = "https://weather-data-api1.p.rapidapi.com/find-location"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"q": q, "limit": limit}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weather-data-api1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
