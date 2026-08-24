import os
import requests

def Monthly_Point_Data(lat, lon, alt, start, end):
    """
    :API_description: This API provides historical weather data for a specified geographic location, including temperature, precipitation, wind speed, and more, aggregated over a given period.
    :param lat: Latitude of the location.
    :param lon: Longitude of the location.
    :param alt: Altitude of the location(optional default is 43).
    :param start: Start date for the data retrieval in YYYY-MM-DD format.
    :param end: End date for the data retrieval in YYYY-MM-DD format.
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
            "description": "Date of the weather data entry."
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
          "wspd": {
            "type": "number",
            "description": "Wind speed for the day."
          },
          "pres": {
            "type": "number",
            "description": "Atmospheric pressure for the day."
          },
          "tsun": {
            "type": "number",
            "description": "Total sunshine duration for the day."
          }
        },
        "required": ["date", "tavg", "tmin", "tmax", "prcp", "wspd", "pres", "tsun"]
      },
      "description": "Array of weather data entries, each containing various weather metrics for a specific date."
    }
  },
  "required": ["meta", "data"]
}
```
    """
    url = "https://meteostat.p.rapidapi.com/point/monthly"
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