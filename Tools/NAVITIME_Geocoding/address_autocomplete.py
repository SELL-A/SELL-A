import os
import requests

def address_autocomplete(word, datum="wgs84", coord_unit="degree"):
    """
    :API_description: Provides address predictions in Tokyo, Japan, based on a keyword input, including geographical details and administrative codes.
    :param word: (str, required) The search term for address autocomplete (e.g., "tok" for Tokyo).
    :param datum: (str, optional) Coordinate system, default is "wgs84".
    :param coord_unit: (str, optional) Unit for coordinates, default is "degree".
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
            "required": ["code", "name", "coord", "details", "is_end"]
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
    url = "https://navitime-geocoding.p.rapidapi.com/address/autocomplete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "datum": datum,
        "word": word,
        "coord_unit": coord_unit
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