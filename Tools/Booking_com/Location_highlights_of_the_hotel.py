import os
import requests

def Location_highlights_of_the_hotel(hotel_id):
    """
    :API_description: Get nearby transportation and landmarks (metro, rail, etc.).
    :param hotel_id: The hotel ID to query location highlights for.
    :response_schema: 
    Summary: The API response provides details about a location's highlights: popular landmarks (list of strings), nearby metro stations (each with distance, type, name), and a restaurant indicator (null). This is typical for a location-based service, possibly for hotels or points of interest.

    Final output.```json
    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "location_highlights": {
          "type": "object",
          "properties": {
            "popular_landmarks": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "List of popular landmarks near the location"
            },
            "nearby_stations": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "distance_meters": {
                    "type": "number",
                    "description": "Distance to the station in meters"
                  },
                  "station_type": {
                    "type": "string",
                    "description": "Type of station (e.g., metro)"
                  },
                  "distance_localized": {
                    "type": "string",
                    "description": "Localized distance string (e.g., '300 m')"
                  },
                  "station_name": {
                    "type": "string",
                    "description": "Name of the station"
                  }
                },
                "required": ["distance_meters", "station_type", "distance_localized", "station_name"]
              },
              "description": "List of nearby metro stations with details"
            },
            "has_restaurant": {
              "type": "array",
              "items": {
                "type": "null"
              },
              "description": "Indicates whether the location has a restaurant (currently null, meaning unknown or not applicable)"
            }
          },
          "required": ["popular_landmarks", "nearby_stations", "has_restaurant"]
        }
      },
      "required": ["location_highlights"]
    }
    ```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/location-highlights"
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