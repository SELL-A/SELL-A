import os
import requests

def Daily_Station_Data(station, start, end):
    """
    :API_description: This API provides historical daily weather data for a specific weather station, including temperature, precipitation, wind, and atmospheric pressure.
    :param station: The ID of the weather station The Meteostat weather station identifier(e.g. "10637").
    :param start: The start date for the data retrieval in YYYY-MM-DD format.
    :param end: The end date for the data retrieval in YYYY-MM-DD format.
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
          "date": {
            "type": "string",
            "format": "date",
            "description": "The date for which the weather data is recorded."
          },
          "tavg": {
            "type": "number",
            "description": "Average temperature for the day."
          },
          "tmin": {
            "type": "number",
            "description": "Minimum temperature for the day."
          },
          "tmax": {
            "type": "number",
            "description": "Maximum temperature for the day."
          },
          "prcp": {
            "type": "number",
            "description": "Precipitation amount for the day."
          },
          "snow": {
            "type": "number",
            "description": "Snowfall amount for the day."
          },
          "wdir": {
            "type": "number",
            "description": "Wind direction in degrees."
          },
          "wspd": {
            "type": "number",
            "description": "Wind speed."
          },
          "wpgt": {
            "type": "number",
            "description": "Peak wind gust."
          },
          "pres": {
            "type": "number",
            "description": "Atmospheric pressure."
          },
          "tsun": {
            "type": "number",
            "description": "Total sunshine duration for the day."
          }
        },
        "required": ["date", "tavg", "tmin", "tmax", "prcp", "snow", "wdir", "wspd", "wpgt", "pres", "tsun"]
      }
    }
  },
  "required": ["meta", "data"]
}
```
    """
    url = "https://meteostat.p.rapidapi.com/stations/daily"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"station": station, "start": start, "end": end}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "meteostat.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

