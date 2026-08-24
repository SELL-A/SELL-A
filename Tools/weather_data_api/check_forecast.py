import os
import requests

def check_forecast(lat, lon):
    """
    :API_description: Retrieve a detailed weather forecast for the National Capital Region in the Philippines, covering 40 data points over 3-hour intervals.
    :param lat: Latitude of the location(the value of 'lat' field returned in find location api response).
    :param lon: Longitude of the location(the value of 'lon' field returned in find location api response).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "cod": {
      "type": "string",
      "description": "HTTP status code"
    },
    "message": {
      "type": "number",
      "description": "Internal parameter"
    },
    "cnt": {
      "type": "number",
      "description": "Number of data points"
    },
    "list": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "dt": {
            "type": "number",
            "description": "Time of data forecasted, unix, UTC"
          },
          "main": {
            "type": "object",
            "properties": {
              "temp": {
                "type": "number",
                "description": "Temperature"
              },
              "feels_like": {
                "type": "number",
                "description": "Temperature perceived"
              },
              "temp_min": {
                "type": "number",
                "description": "Minimum temperature"
              },
              "temp_max": {
                "type": "number",
                "description": "Maximum temperature"
              },
              "pressure": {
                "type": "number",
                "description": "Atmospheric pressure"
              },
              "sea_level": {
                "type": "number",
                "description": "Atmospheric pressure at sea level"
              },
              "grnd_level": {
                "type": "number",
                "description": "Atmospheric pressure at ground level"
              },
              "humidity": {
                "type": "number",
                "description": "Humidity percentage"
              },
              "temp_kf": {
                "type": "number",
                "description": "Internal parameter"
              }
            }
          },
          "weather": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "number",
                  "description": "Weather condition id"
                },
                "main": {
                  "type": "string",
                  "description": "Group of weather parameters"
                },
                "description": {
                  "type": "string",
                  "description": "Weather condition within the group"
                },
                "icon": {
                  "type": "string",
                  "description": "Weather icon id"
                }
              }
            }
          },
          "clouds": {
            "type": "object",
            "properties": {
              "all": {
                "type": "number",
                "description": "Cloudiness percentage"
              }
            }
          },
          "wind": {
            "type": "object",
            "properties": {
              "speed": {
                "type": "number",
                "description": "Wind speed"
              },
              "deg": {
                "type": "number",
                "description": "Wind direction, degrees"
              },
              "gust": {
                "type": "number",
                "description": "Wind gust"
              }
            }
          },
          "visibility": {
            "type": "number",
            "description": "Visibility, meters"
          },
          "pop": {
            "type": "number",
            "description": "Probability of precipitation"
          },
          "rain": {
            "type": "object",
            "properties": {
              "3h": {
                "type": "number",
                "description": "Rain volume for the last 3 hours"
              }
            }
          },
          "sys": {
            "type": "object",
            "properties": {
              "pod": {
                "type": "string",
                "description": "Part of the day (d/n)"
              }
            }
          },
          "dt_txt": {
            "type": "string",
            "description": "Data/time of calculation, UTC"
          }
        }
      }
    },
    "city": {
      "type": "object",
      "properties": {
        "id": {
          "type": "number",
          "description": "City ID"
        },
        "name": {
          "type": "string",
          "description": "City name"
        },
        "coord": {
          "type": "object",
          "properties": {
            "lat": {
              "type": "number",
              "description": "City geo location, latitude"
            },
            "lon": {
              "type": "number",
              "description": "City geo location, longitude"
            }
          }
        },
        "country": {
          "type": "string",
          "description": "Country code"
        },
        "population": {
          "type": "number",
          "description": "City population"
        },
        "timezone": {
          "type": "number",
          "description": "Shift in seconds from UTC"
        },
        "sunrise": {
          "type": "number",
          "description": "Sunrise time, unix, UTC"
        },
        "sunset": {
          "type": "number",
          "description": "Sunset time, unix, UTC"
        }
      }
    }
  }
}
    ```
    """
    url = "https://weather-data-api1.p.rapidapi.com/check-forecast"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"lat": str(lat), "lon": str(lon)}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weather-data-api1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

