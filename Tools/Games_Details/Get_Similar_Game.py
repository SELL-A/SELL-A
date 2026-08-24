import os
import requests

def Get_Similar_Game(id):
    """
    :API_description: Retrieves a list of games similar to a specified title from a Steam-like platform, including details such as game IDs, names, header images, and pricing information.
    :param id: The ID of the game for which similar games are to be retrieved(eg. "124").
    :response_schema: 
    ```json {
  "type": "object",
  "properties": {
    "status": {
      "type": "integer",
      "description": "HTTP status code indicating the success or failure of the API request"
    },
    "message": {
      "type": "string",
      "description": "Human-readable message describing the result of the API call"
    },
    "data": {
      "type": "object",
      "properties": {
        "similar_games": {
          "type": "array",
          "description": "List of game objects that are similar to a reference game",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the game (appears to be Steam app ID)"
              },
              "image": {
                "type": "string",
                "description": "URL to the game's header image/thumbnail"
              },
              "price": {
                "type": "string",
                "description": "Price information - can be monetary value, 'Free To Play', 'Free', or 'comming soon'"
              },
              "name": {
                "type": "string",
                "description": "Full name/title of the game"
              }
            },
            "required": ["id", "image", "price", "name"]
          }
        },
        "total": {
          "type": "integer",
          "description": "Total count of similar games available"
        }
      },
      "required": ["similar_games", "total"]
    }
  },
  "required": ["status", "message", "data"]
}
```
    """
    url = f"https://games-details.p.rapidapi.com/similargame/{id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")