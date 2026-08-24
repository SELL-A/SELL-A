import os
import requests

def Get_Genres():
    """
    :API_description: Retrieves a list of genres for categorizing media content, each identified by a unique identifier.
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "_id": {
        "type": "string",
        "description": "Identifier for the genre or category"
      }
    },
    "required": ["_id"],
    "additionalProperties": false
  }
}
```
    """
    url = "https://anime-db.p.rapidapi.com/genre"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")