import os
import requests

def All_Countries():
    """
    :API_description: Retrieves a comprehensive list of countries with details including names, ISO codes, flag emojis, phone codes, currencies, and timezones.
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "The name of the country."
      },
      "isoCode": {
        "type": "string",
        "description": "The ISO 3166-1 alpha-2 code of the country."
      },
      "flag": {
        "type": "string",
        "description": "The emoji flag of the country."
      },
      "phonecode": {
        "type": "string",
        "description": "The international calling code of the country."
      },
      "currency": {
        "type": "string",
        "description": "The currency code of the country."
      },
      "latitude": {
        "type": "string",
        "description": "The latitude coordinate of the country."
      },
      "longitude": {
        "type": "string",
        "description": "The longitude coordinate of the country."
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
              "description": "The GMT offset name."
            },
            "abbreviation": {
              "type": "string",
              "description": "The timezone abbreviation."
            },
            "tzName": {
              "type": "string",
              "description": "The full name of the timezone."
            }
          },
          "required": ["zoneName", "gmtOffset", "gmtOffsetName", "abbreviation", "tzName"]
        },
        "description": "An array of timezones associated with the country."
      }
    },
    "required": ["name", "isoCode", "flag", "phonecode", "currency", "latitude", "longitude", "timezones"]
  }
}
```
    """
    url = "https://country-state-city-search-rest-api.p.rapidapi.com/allcountries"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "country-state-city-search-rest-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")