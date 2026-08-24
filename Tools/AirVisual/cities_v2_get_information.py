import os
import requests

def cities_v2_get_information(id, x_user_lang=None, x_user_timezone=None, x_aqi_index=None, x_units_pressure=None, x_units_distance=None, x_units_temperature=None):
    """
    :API_description: Retrieve real-time and forecasted air quality and weather data for a specific city by its unique identifier.
    :param id: The unique identifier for the city (optional).
    :param x_user_lang: The language preference for the response (optional).
    :param x_user_timezone: The timezone of the user (optional).
    :param x_aqi_index: The air quality index standard to use (optional).
    :param x_units_pressure: The unit of pressure measurement (optional).
    :param x_units_distance: The unit of distance measurement (optional).
    :param x_units_temperature: The unit of temperature measurement (optional).
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
        "id": {
          "type": "string",
          "description": "Unique identifier for the location or entity."
        },
        "city": {
          "type": "string",
          "description": "Name of the city."
        },
        "state": {
          "type": "string",
          "description": "Name of the state or region."
        },
        "country": {
          "type": "string",
          "description": "Name of the country."
        },
        "location": {
          "type": "object",
          "properties": {
            "lat": {
              "type": "number",
              "description": "Latitude of the location."
            },
            "lon": {
              "type": "number",
              "description": "Longitude of the location."
            }
          },
          "required": ["lat", "lon"]
        },
        "timezone": {
          "type": "string",
          "description": "Timezone of the location."
        },
        "websiteLink": {
          "type": "string",
          "description": "URL to the website related to the location."
        },
        "report": {
          "type": "object",
          "properties": {
            "link": {
              "type": "string",
              "description": "URL to the report page."
            },
            "actionText": {
              "type": "string",
              "description": "Text for the action to report an issue."
            },
            "message": {
              "type": "string",
              "description": "Message encouraging users to report discrepancies."
            }
          },
          "required": ["link", "actionText", "message"]
        },
        "type": {
          "type": "string",
          "description": "Type of the location, e.g., 'city'."
        },
        "name": {
          "type": "string",
          "description": "Name of the location."
        },
        "followers": {
          "type": "object",
          "properties": {
            "total": {
              "type": "string",
              "description": "Total number of followers."
            },
            "pictures": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Array of URLs to follower profile pictures."
            },
            "label": {
              "type": "string",
              "description": "Label displaying the total number of followers."
            }
          },
          "required": ["total", "pictures", "label"]
        },
        "contributors": {
          "type": "object",
          "properties": {
            "pictures": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Array of URLs to contributor profile pictures."
            },
            "redirection": {
              "type": "object",
              "properties": {
                "actionType": {
                  "type": "string",
                  "description": "Type of action for redirection."
                },
                "appCategory": {
                  "type": "string",
                  "description": "Category of the app for redirection."
                },
                "item": {
                  "type": "string",
                  "description": "Item identifier for redirection."
                }
              },
              "required": ["actionType", "appCategory", "item"]
            },
            "label": {
              "type": "string",
              "description": "Label displaying the number of contributors."
            }
          },
          "required": ["pictures", "redirection", "label"]
        },
        "sources": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the source."
              },
              "name": {
                "type": "string",
                "description": "Name of the source."
              },
              "totalStations": {
                "type": "integer",
                "description": "Total number of stations provided by the source."
              },
              "type": {
                "type": "string",
                "description": "Type of the source, e.g., 'source', 'gov'."
              },
              "picture": {
                "type": "string",
                "description": "URL to the source's profile picture."
              },
              "url": {
                "type": "string",
                "description": "URL to the source's website."
              }
            },
            "required": ["id", "name", "totalStations", "type", "picture", "url"]
          },
          "description": "Array of data sources providing information."
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
            "mainus": {
              "type": "string",
              "description": "Main pollutant according to US standards."
            },
            "aqicn": {
              "type": "integer",
              "description": "Air Quality Index (China standard)."
            },
            "maincn": {
              "type": "string",
              "description": "Main pollutant according to China standards."
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
                    "description": "Air Quality Index for the pollutant (US standard)."
                  },
                  "aqicn": {
                    "type": "integer",
                    "description": "Air Quality Index for the pollutant (China standard)."
                  },
                  "pollutant": {
                    "type": "string",
                    "description": "Name of the pollutant."
                  },
                  "isEstimated": {
                    "type": "integer",
                    "description": "Flag indicating if the measurement is estimated."
                  }
                },
                "required": ["conc", "aqius", "aqicn", "pollutant", "isEstimated"]
              },
              "description": "Array of pollutants and their measurements."
            }
          },
          "required": ["ts", "aqius", "mainus", "aqicn", "maincn", "pollutants"]
        },
        "sensorDefinitions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "pollutant": {
                "type": "string",
                "description": "Name of the pollutant."
              },
              "unit": {
                "type": "string",
                "description": "Unit of measurement for the pollutant."
              },
              "name": {
                "type": "string",
                "description": "Name of the sensor."
              }
            },
            "required": ["pollutant", "unit", "name"]
          },
          "description": "Array of sensor definitions."
        },
        "currentWeather": {
          "type": "object",
          "properties": {
            "ts": {
              "type": "string",
              "format": "date-time",
              "description": "Timestamp of the current weather data."
            },
            "temperature": {
              "type": "integer",
              "description": "Current temperature."
            },
            "pressure": {
              "type": "integer",
              "description": "Current atmospheric pressure."
            },
            "humidity": {
              "type": "integer",
              "description": "Current humidity percentage."
            },
            "windSpeed": {
              "type": "number",
              "description": "Current wind speed."
            },
            "windDirection": {
              "type": "integer",
              "description": "Current wind direction in degrees."
            },
            "weatherIcon": {
              "type": "string",
              "description": "Icon representing the current weather condition."
            }
          },
          "required": ["ts", "temperature", "pressure", "humidity", "windSpeed", "windDirection", "weatherIcon"]
        },
        "hourlyForecasts": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "ts": {
                "type": "string",
                "format": "date-time",
                "description": "Timestamp of the forecast."
              },
              "aqius": {
                "type": "integer",
                "description": "Air Quality Index (US standard) forecast."
              },
              "aqicn": {
                "type": "integer",
                "description": "Air Quality Index (China standard) forecast."
              },
              "humidity": {
                "type": "integer",
                "description": "Forecasted humidity percentage."
              },
              "pressure": {
                "type": "integer",
                "description": "Forecasted atmospheric pressure."
              },
              "windSpeed": {
                "type": "number",
                "description": "Forecasted wind speed."
              },
              "windDirection": {
                "type": "integer",
                "description": "Forecasted wind direction in degrees."
              },
              "weatherIcon": {
                "type": "string",
                "description": "Icon representing the forecasted weather condition."
              },
              "temperature": {
                "type": "integer",
                "description": "Forecasted temperature."
              },
              "probabilityOfRain": {
                "type": "integer",
                "description": "Probability of rain."
              }
            },
            "required": ["ts", "aqius", "aqicn", "humidity", "pressure", "windSpeed", "windDirection", "weatherIcon", "temperature"]
          },
          "description": "Array of hourly forecasts."
        }
      },
      "required": ["id", "city", "state", "country", "location", "timezone", "websiteLink", "report", "type", "name", "followers", "contributors", "sources", "currentMeasurement", "sensorDefinitions", "currentWeather", "hourlyForecasts"]
    }
  },
  "required": ["status", "data"]
}
    ```
    """
    url = "https://airvisual1.p.rapidapi.com/cities/v2/get-information"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "id": id,
        "x-user-lang": x_user_lang,
        "x-user-timezone": x_user_timezone,
        "x-aqi-index": x_aqi_index,
        "x-units-pressure": x_units_pressure,
        "x-units-distance": x_units_distance,
        "x-units-temperature": x_units_temperature
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

