import os
import requests

def What_is_here(lat, lng, lang, country):
    """
    :API_description: Retrieve comprehensive details about a specific location, including businesses and their operational status.
    :param lat: Latitude of the location (string).
    :param lng: Longitude of the location (string).
    :param lang: Language for the response (string).
    :param country: Country code for the location (string).
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
        "place_id": {
          "type": "string",
          "description": "Unique identifier for the place."
        },
        "coordinates": {
          "type": "object",
          "properties": {
            "lng": {
              "type": "number",
              "description": "Longitude of the location."
            },
            "lat": {
              "type": "number",
              "description": "Latitude of the location."
            }
          },
          "required": ["lng", "lat"]
        },
        "timezone": {
          "type": "string",
          "description": "Timezone of the location."
        },
        "town": {
          "type": "string",
          "description": "Town or city name."
        },
        "country": {
          "type": "string",
          "description": "Country code."
        },
        "places": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "business_id": {
                "type": "string",
                "description": "Unique identifier for the business."
              },
              "name": {
                "type": "string",
                "description": "Name of the business."
              },
              "full_address": {
                "type": "string",
                "description": "Full address of the business."
              },
              "latitude": {
                "type": "number",
                "description": "Latitude of the business location."
              },
              "longitude": {
                "type": "number",
                "description": "Longitude of the business location."
              },
              "rating": {
                "type": "number",
                "description": "Rating of the business."
              },
              "place_link": {
                "type": "string",
                "description": "URL link to the business on Google Maps."
              },
              "types": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "Types of business or place categories."
              },
              "working_hours": {
                "type": "object",
                "properties": {
                  "Wednesday": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Working hours for Wednesday."
                  },
                  "Thursday": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Working hours for Thursday."
                  },
                  "Friday": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Working hours for Friday."
                  },
                  "Saturday": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Working hours for Saturday."
                  },
                  "Sunday": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Working hours for Sunday."
                  },
                  "Monday": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Working hours for Monday."
                  },
                  "Tuesday": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Working hours for Tuesday."
                  }
                },
                "description": "Working hours for each day of the week."
              },
              "state": {
                "type": "string",
                "description": "Current state of the business (e.g., Open, Closed)."
              }
            },
            "required": ["business_id", "name", "full_address", "latitude", "longitude", "rating", "place_link", "types", "working_hours", "state"]
          },
          "description": "List of businesses or places at the specified location."
        }
      },
      "required": ["address", "place_id", "coordinates", "timezone", "town", "country", "places"]
    }
  },
  "required": ["data"]
}
```
    """
    url = "https://maps-data.p.rapidapi.com/whatishere.php"
    querystring = {"lat": lat, "lng": lng, "lang": lang, "country": country}

    headers = {
        "x-rapidapi-key": "8337d89e37msh71c9e40b4a00012p119156jsnd38901b956f2",
        "x-rapidapi-host": "maps-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")