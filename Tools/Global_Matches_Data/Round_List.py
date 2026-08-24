import os
import requests

def Round_List():
    """
    :API_description: Retrieves a list of rounds or games, each identified by a unique ID, full name, and abbreviated name, suitable for sports leagues or similar events.
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
            "description": "The full name of the round or game."
          },
          "shortName": {
            "type": "string",
            "description": "The abbreviated name of the round or game."
          },
          "id": {
            "type": "integer",
            "description": "A unique identifier for the round or game."
          }
        },
        "required": ["name", "shortName", "id"]
      }
    }
    ```
    """
    url = "https://global-data.p.rapidapi.com/round/list"
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