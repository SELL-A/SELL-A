import os
import requests

def address_code(coord_unit, code, datum):
    """
    :API_description: Retrieve detailed location information including code, name, postal code, coordinates, and hierarchical details based on the provided address code.
    :param coord_unit: Unit of coordinates (e.g., 'degree').
    :param code: Address code to geocode (e.g., '13101001').
    :param datum: Geodetic datum (e.g., 'wgs84').
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "postal_code": {
            "type": "string"
          },
          "coord": {
            "type": "object",
            "properties": {
              "lat": {
                "type": "number"
              },
              "lon": {
                "type": "number"
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
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "ruby": {
                  "type": "string"
                },
                "level": {
                  "type": "string"
                }
              },
              "required": ["code", "name", "ruby", "level"]
            }
          },
          "is_end": {
            "type": "boolean"
          }
        },
        "required": ["code", "name", "postal_code", "coord", "details", "is_end"]
      }
    },
    "unit": {
      "type": "object",
      "properties": {
        "datum": {
          "type": "string"
        },
        "coord_unit": {
          "type": "string"
        }
      },
      "required": ["datum", "coord_unit"]
    }
  },
  "required": ["items", "unit"]
}
```
    """
    url = "https://navitime-geocoding.p.rapidapi.com/address/code"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "coord_unit": coord_unit,
        "code": code,
        "datum": datum
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