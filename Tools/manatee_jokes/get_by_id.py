import os
import requests

def get_by_id(id):
    """
    :API_description: Retrieves a specific joke by its unique ID, including the setup, punchline, and timestamps for creation and last update.
    :param id: The ID of the manatee joke to retrieve.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "Unique identifier for the joke."
    },
    "setup": {
      "type": "string",
      "description": "The setup or lead-in part of the joke."
    },
    "punchline": {
      "type": "string",
      "description": "The punchline or the humorous part of the joke."
    },
    "createdAt": {
      "type": "string",
      "format": "date-time",
      "description": "Timestamp indicating when the joke was created."
    },
    "updatedAt": {
      "type": "string",
      "format": "date-time",
      "description": "Timestamp indicating when the joke was last updated."
    }
  },
  "required": ["id", "setup", "punchline", "createdAt", "updatedAt"]
}
```
    """
    url = f"https://manatee-jokes.p.rapidapi.com/manatees/{id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "manatee-jokes.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")