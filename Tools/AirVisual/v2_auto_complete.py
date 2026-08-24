import os
import requests

def v2_auto_complete(q):
    """
    :API_description: Retrieve detailed air quality data for specified locations, including pollutant concentrations and indices.
    :param q: The query string for the city name.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Status of the API response, typically 'success' or 'error'."
    },
    "data": {
      "type": "object",
      "properties": {
        "cities": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the city."
              },
              "city": {
                "type": "string",
                "description": "Name of the city."
              },
              "state": {
                "type": "string",
                "description": "State or province of the city."
              },
              "country": {
                "type": "string",
                "description": "Country of the city."
              },
              "location": {
                "type": "object",
                "properties": {
                  "lon": {
                    "type": "number",
                    "description": "Longitude of the city's location."
                  },
                  "lat": {
                    "type": "number",
                    "description": "Latitude of the city's location."
                  }
                },
                "required": ["lon", "lat"]
              },
              "currentMeasurement": {
                "type": "object",
                "properties": {
                  "ts": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Timestamp of the current measurement."
                  },
                  "aqius": {
                    "type": "integer",
                    "description": "Air Quality Index (US standard)."
                  },
                  "aqicn": {
                    "type": "integer",
                    "description": "Air Quality Index (China standard)."
                  },
                  "isEstimated": {
                    "type": "integer",
                    "description": "Indicates if the measurement is estimated (0 for false, 1 for true)."
                  }
                },
                "required": ["ts", "aqius", "aqicn", "isEstimated"]
              },
              "sensorDefinitions": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "pollutant": {
                      "type": "string",
                      "description": "Type of pollutant."
                    },
                    "unit": {
                      "type": "string",
                      "description": "Unit of measurement for the pollutant."
                    },
                    "name": {
                      "type": "string",
                      "description": "Name of the pollutant."
                    }
                  },
                  "required": ["pollutant", "unit", "name"]
                }
              },
              "type": {
                "type": "string",
                "description": "Type of location, typically 'city'."
              }
            },
            "required": ["id", "city", "state", "country", "location", "currentMeasurement", "sensorDefinitions", "type"]
          }
        },
        "stations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the station."
              },
              "name": {
                "type": "string",
                "description": "Name of the station."
              },
              "city": {
                "type": "string",
                "description": "City where the station is located."
              },
              "state": {
                "type": "string",
                "description": "State or province where the station is located."
              },
              "country": {
                "type": "string",
                "description": "Country where the station is located."
              },
              "location": {
                "type": "object",
                "properties": {
                  "lon": {
                    "type": "number",
                    "description": "Longitude of the station's location."
                  },
                  "lat": {
                    "type": "number",
                    "description": "Latitude of the station's location."
                  }
                },
                "required": ["lon", "lat"]
              },
              "currentMeasurement": {
                "type": "object",
                "properties": {
                  "ts": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Timestamp of the current measurement."
                  },
                  "aqius": {
                    "type": "integer",
                    "description": "Air Quality Index (US standard)."
                  },
                  "aqicn": {
                    "type": "integer",
                    "description": "Air Quality Index (China standard)."
                  },
                  "pollutants": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "conc": {
                          "type": "number",
                          "description": "Concentration of the pollutant."
                        },
                        "aqius": {
                          "type": "integer",
                          "description": "Air Quality Index (US standard) for the pollutant."
                        },
                        "aqicn": {
                          "type": "integer",
                          "description": "Air Quality Index (China standard) for the pollutant."
                        },
                        "pollutant": {
                          "type": "string",
                          "description": "Type of pollutant."
                        },
                        "isEstimated": {
                          "type": "integer",
                          "description": "Indicates if the measurement is estimated (0 for false, 1 for true)."
                        }
                      },
                      "required": ["conc", "aqius", "aqicn", "pollutant", "isEstimated"]
                    }
                  }
                },
                "required": ["ts", "aqius", "aqicn", "pollutants"]
              },
              "sensorDefinitions": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "pollutant": {
                      "type": "string",
                      "description": "Type of pollutant."
                    },
                    "unit": {
                      "type": "string",
                      "description": "Unit of measurement for the pollutant."
                    },
                    "name": {
                      "type": "string",
                      "description": "Name of the pollutant."
                    }
                  },
                  "required": ["pollutant", "unit", "name"]
                }
              },
              "type": {
                "type": "string",
                "description": "Type of location, typically 'station'."
              }
            },
            "required": ["id", "name", "city", "state", "country", "location", "currentMeasurement", "sensorDefinitions", "type"]
          }
        }
      },
      "required": ["cities", "stations"]
    }
  },
  "required": ["status", "data"]
}
    ```
    """
    url = "https://airvisual1.p.rapidapi.com/v2/auto-complete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "q": q
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "airvisual1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


