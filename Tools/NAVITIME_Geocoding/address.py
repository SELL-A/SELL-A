import os
import requests

def address(word):
    """
    :API_description: Retrieve detailed geographical location data, including names, postal codes, coordinates, and administrative hierarchy, based on search parameters.
    :param word: The search term for the address.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "count": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of items available"
        },
        "offset": {
          "type": "integer",
          "description": "Offset of the current page"
        },
        "limit": {
          "type": "integer",
          "description": "Maximum number of items per page"
        }
      },
      "required": ["total", "offset", "limit"]
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "Unique identifier for the location"
          },
          "name": {
            "type": "string",
            "description": "Name of the location"
          },
          "postal_code": {
            "type": "string",
            "description": "Postal code of the location"
          },
          "coord": {
            "type": "object",
            "properties": {
              "lat": {
                "type": "number",
                "description": "Latitude of the location"
              },
              "lon": {
                "type": "number",
                "description": "Longitude of the location"
              }
            },
            "required": ["lat", "lon"]
          },
          "details": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "string",
                  "description": "Code representing the administrative level"
                },
                "name": {
                  "type": "string",
                  "description": "Name of the administrative level"
                },
                "ruby": {
                  "type": "string",
                  "description": "Ruby (phonetic) representation of the name"
                },
                "level": {
                  "type": "string",
                  "description": "Level of the administrative division"
                }
              },
              "required": ["code", "name", "ruby", "level"]
            }
          },
          "is_end": {
            "type": "boolean",
            "description": "Indicates if this is the last item in the list"
          }
        },
        "required": ["code", "name", "postal_code", "coord", "details", "is_end"]
      }
    },
    "unit": {
      "type": "object",
      "properties": {
        "datum": {
          "type": "string",
          "description": "Coordinate datum system used (e.g., WGS84)"
        },
        "coord_unit": {
          "type": "string",
          "description": "Unit of the coordinates (e.g., degree)"
        }
      },
      "required": ["datum", "coord_unit"]
    }
  },
  "required": ["count", "items", "unit"]
}
```
    """
    url = "https://navitime-geocoding.p.rapidapi.com/address"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "coord_unit": "degree",
        "datum": "wgs84",
        "limit": "10",
        "word": word,
        "sort": "code_asc",
        "offset": "0"
    }
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "navitime-geocoding.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")