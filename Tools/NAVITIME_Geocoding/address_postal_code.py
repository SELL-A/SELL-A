import os
import requests

def address_postal_code(postal_code, datum="wgs84", offset="0", coord_unit="degree", limit="10"):
    """
    :API_description: Retrieve detailed geographical information based on a postal code, including location names, coordinates, and administrative details.
    :param postal_code: The Japanese postal code (e.g., "1510053").
    :param datum: Coordinate datum (default "wgs84").
    :param offset: Offset for pagination (default "0").
    :param coord_unit: Coordinate unit (default "degree").
    :param limit: Maximum number of results (default "10").
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
          "description": "Offset of the current result set"
        },
        "limit": {
          "type": "integer",
          "description": "Maximum number of items returned in the current response"
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
          }
        },
        "required": ["code", "name", "postal_code", "coord", "details"]
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
    url = "https://navitime-geocoding.p.rapidapi.com/address/postal_code"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "datum": datum,
        "offset": offset,
        "coord_unit": coord_unit,
        "limit": limit,
        "postal_code": postal_code
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