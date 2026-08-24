import os
import requests

def airports_list():
    """
    :API_description: Retrieve a comprehensive list of airports worldwide, including details like IATA/ICAO codes, location, timezone, and country information.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string",
      "description": "Version identifier for the data structure."
    },
    "rows": {
      "type": "array",
      "description": "List of airport data entries.",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the airport."
          },
          "name": {
            "type": "string",
            "description": "Name of the airport."
          },
          "iata": {
            "type": "string",
            "description": "IATA code of the airport."
          },
          "icao": {
            "type": "string",
            "description": "ICAO code of the airport."
          },
          "city": {
            "type": "string",
            "description": "City where the airport is located."
          },
          "lat": {
            "type": "number",
            "description": "Latitude coordinate of the airport."
          },
          "lon": {
            "type": "number",
            "description": "Longitude coordinate of the airport."
          },
          "country": {
            "type": "string",
            "description": "Country where the airport is located."
          },
          "alt": {
            "type": "integer",
            "description": "Altitude of the airport in feet."
          },
          "size": {
            "type": "integer",
            "description": "Size of the airport."
          },
          "timezone": {
            "type": "object",
            "description": "Timezone information for the airport.",
            "properties": {
              "name": {
                "type": "string",
                "description": "Name of the timezone."
              },
              "offset": {
                "type": "integer",
                "description": "Offset from UTC in seconds."
              },
              "offsetHours": {
                "type": "string",
                "description": "Offset from UTC in hours and minutes."
              },
              "abbr": {
                "type": "string",
                "description": "Timezone abbreviation."
              },
              "abbrName": {
                "type": "string",
                "description": "Full name of the timezone abbreviation."
              },
              "isDst": {
                "type": "boolean",
                "description": "Indicates if the timezone is currently in Daylight Saving Time."
              }
            },
            "required": ["name", "offset", "offsetHours", "abbr", "abbrName", "isDst"]
          },
          "countryId": {
            "type": "integer",
            "description": "Unique identifier for the country."
          }
        },
        "required": ["id", "name", "iata", "icao", "city", "lat", "lon", "country", "alt", "size", "timezone", "countryId"]
      }
    }
  },
  "required": ["version", "rows"]
}
    ```
    """
    url = "https://flight-radar1.p.rapidapi.com/airports/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "flight-radar1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    results = airports_list()
    print(results)