import os
import requests

def Daily_Point_Data(lat, lon, alt, start, end):
    """
    :API_description: This endpoint retrieves historical weather data for a specified geographic location, including temperature, precipitation, and wind statistics.
    :param lat: Latitude of the location.
    :param lon: Longitude of the location.
    :param alt: Altitude of the location(optional default is 184).
    :param start: Start date for the weather data in YYYY-MM-DD format.
    :param end: End date for the weather data in YYYY-MM-DD format.
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
          "description": "Timestamp when the data was generated."
        },
        "stations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of station identifiers."
        }
      },
      "required": ["generated", "stations"]
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "date": {
            "type": "string",
            "format": "date",
            "description": "Date of the weather data."
          },
          "tavg": {
            "type": "number",
            "description": "Average temperature."
          },
          "tmin": {
            "type": "number",
            "description": "Minimum temperature."
          },
          "tmax": {
            "type": "number",
            "description": "Maximum temperature."
          },
          "prcp": {
            "type": "number",
            "description": "Precipitation amount."
          },
          "snow": {
            "type": "number",
            "description": "Snowfall amount."
          },
          "wdir": {
            "type": "number",
            "description": "Wind direction."
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
            "type": ["number", "null"],
            "description": "Total sunshine duration."
          }
        },
        "required": ["date", "tavg", "tmin", "tmax", "prcp", "snow", "wdir", "wspd", "wpgt", "pres", "tsun"]
      },
      "description": "Array of weather data entries."
    }
  },
  "required": ["meta", "data"]
}
    ```
    """
    url = "https://meteostat.p.rapidapi.com/point/daily"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"lat": lat, "lon": lon, "alt": alt, "start": start, "end": end}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "meteostat.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

