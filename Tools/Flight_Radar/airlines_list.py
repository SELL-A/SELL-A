import os
import requests

def airlines_list():
    """
    :API_description: Retrieve a list of airlines, including their names, codes, and ICAO codes.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "integer",
      "description": "The version number of the API response."
    },
    "rows": {
      "type": "array",
      "description": "An array of airline data entries.",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string",
            "description": "The name of the airline."
          },
          "Code": {
            "type": "string",
            "description": "The airline code."
          },
          "ICAO": {
            "type": "string",
            "description": "The ICAO code of the airline."
          }
        },
        "required": ["Name", "Code", "ICAO"]
      }
    }
  },
  "required": ["version", "rows"]
}
```
    """
    url = "https://flight-radar1.p.rapidapi.com/airlines/list"
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
        
