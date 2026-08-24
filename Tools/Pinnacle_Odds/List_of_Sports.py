import os
import requests

def List_of_Sports():
    """
    :API_description: Retrieve a list of sports, each identified by a unique ID and parent ID, along with their names and event timestamps.
    :param: None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "integer",
        "description": "Unique identifier for the sport."
      },
      "p_id": {
        "type": "integer",
        "description": "Parent identifier, possibly linking to a broader category or group."
      },
      "name": {
        "type": "string",
        "description": "Name of the sport."
      },
      "last_call": {
        "type": "integer",
        "description": "Timestamp of the last API call related to this sport."
      },
      "last": {
        "type": "integer",
        "description": "Timestamp of the last event or update for this sport."
      },
      "special_last": {
        "type": "integer",
        "description": "Timestamp of a special or significant last event for this sport."
      }
    },
    "required": ["id", "p_id", "name", "last_call", "last", "special_last"]
  }
}
    ```
    """
    url = "https://pinnacle-odds.p.rapidapi.com/kit/v1/sports"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
