import os
import requests

def States_By_Country_Code(countrycode):
    """
    :API_description: Retrieve a list of states and territories within a specified country, including their names, ISO codes, and geographical coordinates.
    :param countrycode: The code of the country for which to retrieve states(eg: "us").
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "The name of the state or territory."
      },
      "isoCode": {
        "type": "string",
        "description": "The ISO code representing the state or territory."
      },
      "countryCode": {
        "type": "string",
        "description": "The ISO code representing the country."
      },
      "latitude": {
        "type": "string",
        "description": "The latitude coordinate of the state or territory."
      },
      "longitude": {
        "type": "string",
        "description": "The longitude coordinate of the state or territory."
      }
    },
    "required": ["name", "isoCode", "countryCode", "latitude", "longitude"]
  }
}
```
    """
    url = "https://country-state-city-search-rest-api.p.rapidapi.com/states-by-countrycode"
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