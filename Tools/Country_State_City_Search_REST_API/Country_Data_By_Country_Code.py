import os
import requests

def Country_Data_By_Country_Code(countrycode):
    """
    :API_description: Retrieves comprehensive country information based on the provided ISO country code, including name, flag, phone code, currency, and timezones.
    :param countrycode: The code of the country for which data is being requested(eg: "us").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the country."
    },
    "isoCode": {
      "type": "string",
      "description": "The ISO code representing the country."
    },
    "flag": {
      "type": "string",
      "description": "The emoji flag representing the country."
    },
    "phonecode": {
      "type": "string",
      "description": "The phone code of the country."
    },
    "currency": {
      "type": "string",
      "description": "The currency code used in the country."
    },
    "latitude": {
      "type": "string",
      "description": "The latitude coordinate of the country's geographical center."
    },
    "longitude": {
      "type": "string",
      "description": "The longitude coordinate of the country's geographical center."
    },
    "timezones": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "zoneName": {
            "type": "string",
            "description": "The name of the timezone."
          },
          "gmtOffset": {
            "type": "integer",
            "description": "The GMT offset in seconds."
          },
          "gmtOffsetName": {
            "type": "string",
            "description": "The GMT offset name in the format UTC±HH:MM."
          },
          "abbreviation": {
            "type": "string",
            "description": "The abbreviation of the timezone."
          },
          "tzName": {
            "type": "string",
            "description": "The full name of the timezone."
          }
        },
        "required": ["zoneName", "gmtOffset", "gmtOffsetName", "abbreviation", "tzName"]
      },
      "description": "An array of timezones applicable to the country."
    }
  },
  "required": ["name", "isoCode", "flag", "phonecode", "currency", "latitude", "longitude", "timezones"]
}
    ```
    """
    url = "https://country-state-city-search-rest-api.p.rapidapi.com/country-data-by-countrycode"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"countrycode": countrycode}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "country-state-city-search-rest-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")