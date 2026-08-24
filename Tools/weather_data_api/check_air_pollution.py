import os
import requests

def check_air_pollution(lat, lon):
    """
    :API_description: Retrieve detailed air quality data for a specific location, including pollutant concentrations and Air Quality Index (AQI).
    :param lat: Latitude of the location(the value of 'lat' field returned in find location api response).
    :param lon: Longitude of the location(the value of 'lon' field returned in find location api response).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "coord": {
      "type": "object",
      "properties": {
        "lon": {
          "type": "number",
          "description": "Longitude of the location"
        },
        "lat": {
          "type": "number",
          "description": "Latitude of the location"
        }
      },
      "required": ["lon", "lat"]
    },
    "list": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "main": {
            "type": "object",
            "properties": {
              "aqi": {
                "type": "integer",
                "description": "Air Quality Index"
              }
            },
            "required": ["aqi"]
          },
          "components": {
            "type": "object",
            "properties": {
              "co": {
                "type": "number",
                "description": "Concentration of Carbon Monoxide"
              },
              "no": {
                "type": "number",
                "description": "Concentration of Nitric Oxide"
              },
              "no2": {
                "type": "number",
                "description": "Concentration of Nitrogen Dioxide"
              },
              "o3": {
                "type": "number",
                "description": "Concentration of Ozone"
              },
              "so2": {
                "type": "number",
                "description": "Concentration of Sulfur Dioxide"
              },
              "pm2_5": {
                "type": "number",
                "description": "Concentration of Particulate Matter <2.5 micrometers"
              },
              "pm10": {
                "type": "number",
                "description": "Concentration of Particulate Matter <10 micrometers"
              },
              "nh3": {
                "type": "number",
                "description": "Concentration of Ammonia"
              }
            },
            "required": ["co", "no", "no2", "o3", "so2", "pm2_5", "pm10", "nh3"]
          },
          "dt": {
            "type": "integer",
            "description": "Timestamp of the data collection"
          }
        },
        "required": ["main", "components", "dt"]
      }
    }
  },
  "required": ["coord", "list"]
}
```
    """
    url = "https://weather-data-api1.p.rapidapi.com/air_pollution"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"lat": lat, "lon": lon}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weather-data-api1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

