import os
import requests

def aircrafts_list():
    """
    :API_description: Retrieve a list of aircraft families and their models, each identified by a unique code.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "integer",
      "description": "The version number of the data structure."
    },
    "rows": {
      "type": "array",
      "description": "An array of aircraft family objects.",
      "items": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string",
            "description": "A description of the aircraft family."
          },
          "models": {
            "type": "array",
            "description": "An array of aircraft models within the family.",
            "items": {
              "type": "object",
              "properties": {
                "Name": {
                  "type": "string",
                  "description": "The name of the aircraft model."
                },
                "Code": {
                  "type": "string",
                  "description": "The code associated with the aircraft model."
                }
              },
              "required": ["Name", "Code"]
            }
          }
        },
        "required": ["description", "models"]
      }
    }
  },
  "required": ["version", "rows"]
}
```
    """
    url = "https://flight-radar1.p.rapidapi.com/aircrafts/list"
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