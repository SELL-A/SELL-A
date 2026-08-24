import os
import requests

def Status_List():
    """
    :API_description: Retrieves a list of statuses or events related to sports matches, including full names, abbreviations, and unique identifiers.
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
            "description": "The full name of the event or status."
          },
          "shortName": {
            "type": "string",
            "description": "The abbreviated name of the event or status."
          },
          "id": {
            "type": "integer",
            "description": "A unique identifier for the event or status."
          }
        },
        "required": ["name", "shortName", "id"]
      }
    }
    ```
    """
    url = "https://global-data.p.rapidapi.com/status/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "global-data.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")