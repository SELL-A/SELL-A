import os
import requests

def Search_Nearby(query, lat, lng):
    """
    :API_description: Retrieve detailed information about cafes and restaurants in Paris, including business ID, contact details, location, ratings, operating hours, and photos.
    :param query: The search term, e.g., 'cafe'.
    :param lat: Latitude of the location.
    :param lng: Longitude of the location.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "business_id": {
            "type": "string"
          },
          "phone_number": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "full_address": {
            "type": "string"
          },
          "latitude": {
            "type": "number"
          },
          "longitude": {
            "type": "number"
          },
          "review_count": {
            "type": "integer"
          },
          "rating": {
            "type": "number"
          },
          "timezone": {
            "type": "string"
          },
          "website": {
            "type": ["string", "null"]
          },
          "place_id": {
            "type": "string"
          },
          "place_link": {
            "type": "string"
          },
          "types": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "price_level": {
            "type": "string"
          },
          "working_hours": {
            "type": "object",
            "properties": {
              "Wednesday": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "Thursday": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "Friday": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "Saturday": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "Sunday": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "Monday": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "Tuesday": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            },
            "required": ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
          },
          "city": {
            "type": "string"
          },
          "photos": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "src": {
                  "type": "string"
                },
                "max_size": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  }
                },
                "min_size": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  }
                }
              },
              "required": ["src", "max_size", "min_size"]
            }
          },
          "state": {
            "type": "string"
          },
          "description": {
            "type": "array",
            "items": {
              "type": ["string", "null"]
            }
          }
        },
        "required": ["business_id", "phone_number", "name", "full_address", "latitude", "longitude", "review_count", "rating", "timezone", "website", "place_id", "place_link", "types", "price_level", "working_hours", "city", "photos", "state", "description"]
      }
    }
  },
  "required": ["data"]
}
```
    """
    url = "https://maps-data.p.rapidapi.com/nearby.php"
    querystring = {
        "query": query,
        "lat": lat,
        "lng": lng
    }

    headers = {
        "x-rapidapi-key": "8337d89e37msh71c9e40b4a00012p119156jsnd38901b956f2",
        "x-rapidapi-host": "maps-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")