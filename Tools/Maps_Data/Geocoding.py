import os
import requests

def Geocoding(query):
    """
    :API_description: Retrieve detailed location information including full address, latitude, longitude, and timezone based on an address query.
    :param query: The name of the place to be geocoded.
  
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "address": {
              "type": "string",
              "description": "The full address of the location."
            },
            "lat": {
              "type": "number",
              "description": "The latitude coordinate of the location."
            },
            "lng": {
              "type": "number",
              "description": "The longitude coordinate of the location."
            },
            "timezone": {
              "type": "string",
              "description": "The timezone identifier for the location."
            }
          },
          "required": ["address", "lat", "lng", "timezone"]
        }
      },
      "required": ["data"]
    }
    ```
    """
    url = "https://maps-data.p.rapidapi.com/geocoding.php"
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": "8337d89e37msh71c9e40b4a00012p119156jsnd38901b956f2",
        "x-rapidapi-host": "maps-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

