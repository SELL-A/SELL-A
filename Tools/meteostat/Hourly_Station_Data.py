import os
import requests

def Hourly_Station_Data(station, start, end, tz):
    """
    :API_description: This endpoint provides detailed historical hourly weather observations for a specified weather station, including temperature, humidity, and wind data.
    :param station: The ID of the weather station.
    :param start: The start date for the data retrieval in YYYY-MM-DD format.
    :param end: The end date for the data retrieval in YYYY-MM-DD format.
    :param tz: The timezone for the data(optional default is "UTC")(e.g. "America/Toronto").
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
          "format": "date-time",
          "description": "Timestamp indicating when the data was generated."
        }
      },
      "required": ["generated"]
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "time": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp indicating the time of the weather data entry."
          },
          "temp": {
            "type": "number",
            "description": "Temperature in degrees Celsius."
          },
          "dwpt": {
            "type": "number",
            "description": "Dew point temperature in degrees Celsius."
          },
          "rhum": {
            "type": "number",
            "description": "Relative humidity as a percentage."
          },
          "prcp": {
            "type": "number",
            "description": "Precipitation amount in millimeters."
          },
          "snow": {
            "type": ["number", "null"],
            "description": "Snowfall amount in millimeters."
          },
          "wdir": {
            "type": "number",
            "description": "Wind direction in degrees."
          },
          "wspd": {
            "type": "number",
            "description": "Wind speed in meters per second."
          },
          "wpgt": {
            "type": "number",
            "description": "Peak wind gust in meters per second."
          },
          "pres": {
            "type": "number",
            "description": "Atmospheric pressure in hPa."
          },
          "tsun": {
            "type": "number",
            "description": "Total sunshine duration in minutes."
          },
          "coco": {
            "type": "number",
            "description": "Weather condition code."
          }
        },
        "required": ["time", "temp", "dwpt", "rhum", "prcp", "snow", "wdir", "wspd", "wpgt", "pres", "tsun", "coco"]
      }
    }
  },
  "required": ["meta", "data"]
}
```
    """
    url = "https://meteostat.p.rapidapi.com/stations/hourly"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"station": station, "start": start, "end": end, "tz": tz}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "meteostat.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")