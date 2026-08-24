import os
import requests

def Get_Nearby_cities(latitude, longitude):
    """
    :API_description: This API returns a list of nearby cities with hotel availability, sorted by distance from a specified geographic coordinate. Each result includes location details, region information, and the count of available hotels.
    :param latitude: The latitude of the location to find nearby cities Default: -18.5333.
    :param longitude: The longitude of the location to find nearby cities Default: 65.9667.
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "dest_id": {
        "type": "integer",
        "description": "Unique identifier for the destination (can be negative integers or positive integers like 900052591)"
      },
      "nr_hotels": {
        "type": "integer",
        "description": "Number of hotels available in the destination"
      },
      "country": {
        "type": "string",
        "description": "Country name where the destination is located"
      },
      "cc1": {
        "type": "string",
        "description": "Country code (2-character format)"
      },
      "longitude": {
        "type": "number",
        "description": "Geographical longitude coordinate of the destination"
      },
      "dest_type": {
        "type": "string",
        "description": "Type of destination (e.g., 'city')"
      },
      "name": {
        "type": "string",
        "description": "Name of the destination"
      },
      "region": {
        "type": "string",
        "description": "Geographical region within the country"
      },
      "distance": {
        "type": "number",
        "description": "Distance value (likely from a reference point)"
      },
      "latitude": {
        "type": "number",
        "description": "Geographical latitude coordinate of the destination"
      }
    },
    "required": [
      "dest_id",
      "nr_hotels",
      "country",
      "cc1",
      "longitude",
      "dest_type",
      "name",
      "region",
      "distance",
      "latitude"
    ],
    "additionalProperties": false
  }
}
```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/nearby-cities"
    querystring = {
        "locale": "en-us",
        "latitude": latitude,
        "longitude": longitude,
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