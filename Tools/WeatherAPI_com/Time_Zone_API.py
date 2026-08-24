import os
import requests

def Time_Zone_API(location):
    """
    :API_description: Retrieve detailed time zone and local time information for a specified location, supporting various query formats.
    :param location: The location for which the timezone information is requested.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "location": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the location."
        },
        "region": {
          "type": "string",
          "description": "The region of the location."
        },
        "country": {
          "type": "string",
          "description": "The country of the location."
        },
        "lat": {
          "type": "number",
          "description": "The latitude of the location."
        },
        "lon": {
          "type": "number",
          "description": "The longitude of the location."
        },
        "tz_id": {
          "type": "string",
          "description": "The timezone ID of the location."
        },
        "localtime_epoch": {
          "type": "integer",
          "description": "The local time of the location in epoch format."
        },
        "localtime": {
          "type": "string",
          "description": "The local time of the location in ISO 8601 format."
        }
      },
      "required": ["name", "region", "country", "lat", "lon", "tz_id", "localtime_epoch", "localtime"]
    }
  },
  "required": ["location"]
}
```
    """
    url = "https://weatherapi-com.p.rapidapi.com/timezone.json"
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
        
