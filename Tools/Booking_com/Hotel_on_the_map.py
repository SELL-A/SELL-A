import os
import requests

def Hotel_on_the_map(hotel_id):
    """
    :API_description: Get geographic coordinates and nearby landmarks.
    :param hotel_id: The ID of the hotel to fetch map markers for.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "geo_info": {
      "type": "object",
      "description": "Geographic information about the location",
      "properties": {
        "city_centre": {
          "type": "object",
          "description": "Distance and coordinates of the city centre relative to the location",
          "properties": {
            "distance": { "type": "string", "description": "Distance to city centre in meters (as string)" },
            "latitude": { "type": "number" },
            "longitude": { "type": "number" }
          }
        },
        "nearest_airport_info": {
          "type": "object",
          "description": "Latitude, longitude and distance of the nearest airport",
          "properties": {
            "latitude": { "type": "number" },
            "distance": { "type": "string", "description": "Distance to airport in meters (as string)" },
            "longitude": { "type": "number" }
          }
        }
      }
    },
    "landmarks": {
      "type": "array",
      "description": "List of nearby landmarks (currently empty)",
      "items": {}
    },
    "map_preview_url": {
      "type": "string",
      "description": "URL to a static map preview image from Google Maps"
    }
  }
}
```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/map-markers"
    querystring = {
        "locale": "en-us",
        "hotel_id": hotel_id
    }
    headers = {
        "x-rapidapi-key": "8337d89e37msh71c9e40b4a00012p119156jsnd38901b956f2",
        "x-rapidapi-host": "booking-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")