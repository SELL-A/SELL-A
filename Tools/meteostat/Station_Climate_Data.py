import os
import requests

def Station_Climate_Data(station, start, end):
    """
    :API_description: Retrieve detailed meteorological data for a specific weather station, including temperature, precipitation, wind speed, and more.
    :param station: The ID of the weather station The Meteostat weather station identifier(e.g. "10637").
    :param start: The start year for the climate normals.
    :param end: The end year for the climate normals.
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
            "type": "number",
            "description": "Average wind speed for the month."
          },
          "pres": {
            "type": "number",
            "description": "Average atmospheric pressure for the month."
          },
          "tsun": {
            "type": "number",
            "description": "Total sunshine duration for the month."
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
    url = "https://meteostat.p.rapidapi.com/stations/normals"
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