import os
import requests

def cities_v2_get_measurements(id, x_user_lang=None, x_user_timezone=None, x_aqi_index=None, x_units_pressure=None, x_units_distance=None, x_units_temperature=None):
    """
    :API_description: Retrieve air quality measurements for a specific city by its ID, including data on pollutants like PM2.5, PM10, O3, NO2, SO2, and CO.
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
          "description": "Unique identifier for the data set."
        },
        "hourlyMeasurements": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "ts": {
                "type": "string",
                "format": "date-time",
                "description": "Timestamp indicating the time of the measurement."
              },
              "measurements": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "value": {
                      "type": "number",
                      "description": "Numeric value of the measurement."
                    },
                    "measure": {
                      "type": "string",
                      "description": "Type of measurement, e.g., 'pm25', 'aqius', etc."
                    },
                    "color": {
                      "type": "string",
                      "description": "Color code indicating the quality of the measurement."
                    },
                    "label": {
                      "type": "string",
                      "description": "Label describing the quality of the measurement, e.g., 'Moderate', 'Good'."
                    }
                  },
                  "required": ["value", "measure", "color", "label"]
                }
              }
            },
            "required": ["ts", "measurements"]
          }
        }
      },
      "required": ["id", "hourlyMeasurements"]
    }
  },
  "required": ["status", "data"]
}
```
    """
    url = "https://airvisual1.p.rapidapi.com/cities/v2/get-measurements"
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