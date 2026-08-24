import os
import requests

def Cities_By_Country_Code(countrycode):
    """
    :API_description: Retrieve a list of cities in a specified country, including details like city name, country code, state code, and geographical coordinates.
    :param countrycode: The ISO code of the country for which cities are to be retrieved(eg: "us").
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "The name of the location."
      },
      "countryCode": {
        "type": "string",
        "description": "The country code of the location."
      },
      "stateCode": {
        "type": "string",
        "description": "The state code of the location."
      },
      "latitude": {
        "type": "string",
        "description": "The latitude coordinate of the location."
      },
      "longitude": {
        "type": "string",
        "description": "The longitude coordinate of the location."
      }
    },
    "required": ["name", "countryCode", "stateCode", "latitude", "longitude"]
  }
}
```
    """
    url = "https://country-state-city-search-rest-api.p.rapidapi.com/cities-by-countrycode"
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