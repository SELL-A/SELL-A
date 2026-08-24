import os
import requests

def Point_Climate_Data(lat, lon, alt, start, end):
    """
    :API_description: This API provides historical weather data for specified locations, including temperature, precipitation, and sunshine duration.
    :param lat: Latitude of the location.
    :param lon: Longitude of the location.
    :param alt: Altitude of the location.
    :param start: Start year for the climate normals.
    :param end: End year for the climate normals.
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
          "month": {
            "type": "integer",
            "description": "Month of the year (1-12)."
          },
          "tavg": {
            "type": "number",
            "description": "Average temperature for the month."
          },
          "tmin": {
            "type": "number",
            "description": "Minimum temperature for the month."
          },
          "tmax": {
            "type": "number",
            "description": "Maximum temperature for the month."
          },
          "prcp": {
            "type": "number",
            "description": "Precipitation amount for the month."
          },
          "wspd": {
            "type": ["number", "null"],
            "description": "Wind speed for the month (null if not available)."
          },
          "pres": {
            "type": "number",
            "description": "Atmospheric pressure for the month."
          },
          "tsun": {
            "type": "integer",
            "description": "Total sunshine duration for the month in minutes."
          }
        },
        "required": ["month", "tavg", "tmin", "tmax", "prcp", "wspd", "pres", "tsun"]
      }
    }
  },
  "required": ["meta", "data"]
}
```
    """
    url = "https://meteostat.p.rapidapi.com/point/normals"
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
