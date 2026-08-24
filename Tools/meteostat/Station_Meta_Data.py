import os
import requests

def Station_Meta_Data(id):
    """
    :API_description: This endpoint provides detailed metadata for a specific weather station, including identifiers, geographical coordinates, timezone, and historical data availability.
    :param id: The unique identifier for the weather station The Meteostat weather station identifier(e.g. "10637").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "meta": {
      "type": "object",
      "properties": {
        "generated": {
          "type": "string",
          "format": "date-time"
        }
      },
      "required": ["generated"]
    },
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "object",
          "properties": {
            "de": {
              "type": "string"
            },
            "es": {
              "type": "string"
            },
            "en": {
              "type": "string"
            }
          },
          "required": ["de", "es", "en"]
        },
        "country": {
          "type": "string"
        },
        "region": {
          "type": "string"
        },
        "identifier": {
          "type": "object",
          "properties": {
            "national": {
              "type": "string"
            },
            "wmo": {
              "type": "string"
            },
            "icao": {
              "type": "string"
            }
          },
          "required": ["national", "wmo", "icao"]
        },
        "location": {
          "type": "object",
          "properties": {
            "latitude": {
              "type": "number"
            },
            "longitude": {
              "type": "number"
            },
            "elevation": {
              "type": "number"
            }
          },
          "required": ["latitude", "longitude", "elevation"]
        },
        "timezone": {
          "type": "string"
        },
        "inventory": {
          "type": "object",
          "properties": {
            "model": {
              "type": "object",
              "properties": {
                "start": {
                  "type": "string",
                  "format": "date"
                },
                "end": {
                  "type": "string",
                  "format": "date"
                }
              },
              "required": ["start", "end"]
            },
            "hourly": {
              "type": "object",
              "properties": {
                "start": {
                  "type": "string",
                  "format": "date"
                },
                "end": {
                  "type": "string",
                  "format": "date"
                }
              },
              "required": ["start", "end"]
            },
            "daily": {
              "type": "object",
              "properties": {
                "start": {
                  "type": "string",
                  "format": "date"
                },
                "end": {
                  "type": "string",
                  "format": "date"
                }
              },
              "required": ["start", "end"]
            },
            "monthly": {
              "type": "object",
              "properties": {
                "start": {
                  "type": "integer"
                },
                "end": {
                  "type": "integer"
                }
              },
              "required": ["start", "end"]
            },
            "normals": {
              "type": "object",
              "properties": {
                "start": {
                  "type": "integer"
                },
                "end": {
                  "type": "integer"
                }
              },
              "required": ["start", "end"]
            }
          },
          "required": ["model", "hourly", "daily", "monthly", "normals"]
        }
      },
      "required": ["id", "name", "country", "region", "identifier", "location", "timezone", "inventory"]
    }
  },
  "required": ["meta", "data"]
}
    ```
    """
    url = "https://meteostat.p.rapidapi.com/stations/meta"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "meteostat.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")