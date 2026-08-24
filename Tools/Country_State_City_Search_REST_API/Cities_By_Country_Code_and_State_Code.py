import os
import requests

def Cities_By_Country_Code_and_State_Code(countrycode, statecode):
    """
    :API_description: Retrieve a list of cities in a specified state and country, including their names and geographical coordinates.
    :param countrycode: The code representing the country (e.g., 'us' for the United States).
    :param statecode: The code representing the state within the country (e.g., 'fl' for Florida).
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
        "description": "The ISO 3166-1 alpha-2 country code."
      },
      "stateCode": {
        "type": "string",
        "description": "The ISO 3166-2 state/province code."
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
    url = "https://country-state-city-search-rest-api.p.rapidapi.com/cities-by-countrycode-and-statecode"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"countrycode": countrycode, "statecode": statecode}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "country-state-city-search-rest-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")