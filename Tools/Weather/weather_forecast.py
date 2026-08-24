import os
import requests

def weather_forecast(date, language, latitude, longitude, units):
    """
    :API_description: Retrieve detailed weather and health forecasts for a specific geographical location, including daily health risks and historical weather summaries.
    :param date: The date for which the weather forecast is requested (format: YYYYMMDD).
    :param language: The language in which the weather information should be returned(e.g., "en-US" for English in the United States).
    :param latitude: The latitude of the location for which the weather forecast is requested.
    :param longitude: The longitude of the location for which the weather forecast is requested.
    :param units: The units of measurement for the weather data (e.g., metric or imperial).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Geographical coordinates in the format 'latitude,longitude'."
    },
    "v3-wx-forecast-daily-15day-cognitiveHealth": {
      "type": "object",
      "properties": {
        "migraine": {
          "type": "object",
          "properties": {
            "riskLevel": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of risk levels for migraine over the next 15 days."
            },
            "expirationTimeUtc": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of expiration times in UTC for the migraine risk levels."
            },
            "validTimeUtc": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of valid times in UTC for the migraine risk levels."
            }
          }
        },
        "coldAndFlu": {
          "type": "object",
          "properties": {
            "riskLevel": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of risk levels for cold and flu over the next 15 days."
            },
            "expirationTimeUtc": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of expiration times in UTC for the cold and flu risk levels."
            },
            "validTimeUtc": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of valid times in UTC for the cold and flu risk levels."
            }
          }
        },
        "pain": {
          "type": "object",
          "properties": {
            "riskLevel": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of risk levels for pain over the next 15 days."
            },
            "expirationTimeUtc": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of expiration times in UTC for the pain risk levels."
            },
            "validTimeUtc": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of valid times in UTC for the pain risk levels."
            }
          }
        },
        "allergies": {
          "type": "object",
          "properties": {
            "riskLevel": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of risk levels for allergies over the next 15 days."
            },
            "expirationTimeUtc": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of expiration times in UTC for the allergies risk levels."
            },
            "validTimeUtc": {
              "type": "array",
              "items": {
                "type": ["integer", "null"]
              },
              "description": "Array of valid times in UTC for the allergies risk levels."
            }
          }
        }
      }
    },
    "v3-wx-conditions-historical-dailysummary-30day": {
      "type": "object",
      "properties": {
        "dayOfWeek": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Array of days of the week for the historical daily summary."
        },
        "iconCodeDay": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of icon codes for daytime weather conditions."
        },
        "iconCodeExtendDay": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of extended icon codes for daytime weather conditions."
        },
        "iconCodeExtendNight": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of extended icon codes for nighttime weather conditions."
        },
        "iconCodeNight": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of icon codes for nighttime weather conditions."
        },
        "precip24Hour": {
          "type": "array",
          "items": {
            "type": "number"
          },
          "description": "Array of 24-hour precipitation amounts."
        },
        "rain24Hour": {
          "type": "array",
          "items": {
            "type": "number"
          },
          "description": "Array of 24-hour rain amounts."
        },
        "snow24Hour": {
          "type": "array",
          "items": {
            "type": "number"
          },
          "description": "Array of 24-hour snow amounts."
        },
        "temperatureMax": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of maximum temperatures."
        },
        "temperatureMin": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of minimum temperatures."
        },
        "validTimeLocal": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "date-time"
          },
          "description": "Array of valid times in local time."
        },
        "validTimeUtc": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of valid times in UTC."
        },
        "wxPhraseLongDay": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Array of long weather phrases for daytime conditions."
        },
        "wxPhraseLongNight": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Array of long weather phrases for nighttime conditions."
        }
      }
    },
    "v3-wx-forecast-hourly-10day": {
      "type": "object",
      "properties": {
        "cloudCover": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of cloud cover percentages."
        },
        "dayOfWeek": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Array of days of the week for the hourly forecast."
        },
        "dayOrNight": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Array indicating whether the forecast is for day ('D') or night ('N')."
        }
      }
    }
  }
}
    ```
    """
    url = "https://weather338.p.rapidapi.com/weather/forecast"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "date": date,
        "language": language,
        "latitude": latitude,
        "longitude": longitude,
        "units": units
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weather338.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")