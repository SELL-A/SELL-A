import os
import requests

def stations_v2_get_measurements(id, x_user_lang="en-US", x_aqi_index="us", x_units_pressure="mbar", x_units_distance="kilometer", x_user_timezone="Asia/Singapore", x_units_temperature="celsius"):
    """
    :API_description: Retrieve detailed hourly air quality measurements for a specific station by its ID, including pollutants like PM2.5, PM10, O3, NO2, SO2, and CO.
    :param id: The unique identifier for the station.
    :param x_user_lang: Language preference for the response (optional).
    :param x_aqi_index: Air Quality Index standard (optional).
    :param x_units_pressure: Units for pressure measurement (optional).
    :param x_units_distance: Units for distance measurement (optional).
    :param x_user_timezone: User's timezone (optional).
    :param x_units_temperature: Units for temperature measurement (optional).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Indicates the status of the API response, typically 'success' or 'error'."
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
                      "description": "Label describing the quality of the measurement, e.g., 'Moderate', 'Good', etc."
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
    url = "https://airvisual1.p.rapidapi.com/stations/v2/get-measurements"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "x-user-lang": x_user_lang,
        "x-aqi-index": x_aqi_index,
        "x-units-pressure": x_units_pressure,
        "id": id,
        "x-units-distance": x_units_distance,
        "x-user-timezone": x_user_timezone,
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