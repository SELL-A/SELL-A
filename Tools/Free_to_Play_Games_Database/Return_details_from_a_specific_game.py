import os
import requests

def Return_details_from_a_specific_game(game_id):
    """
    :API_description: Get detailed information for a specific game by its ID.
    :param game_id: The unique identifier of the game to retrieve details for.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "id": {"type": "integer", "description": "Unique identifier for the game"},
    "title": {"type": "string", "description": "Title of the game"},
    "thumbnail": {"type": "string", "format": "uri", "description": "URL to the game's thumbnail image"},
    "status": {"type": "string", "description": "Current status of the game (e.g., Live, Beta)"},
    "short_description": {"type": "string", "description": "Short description or tagline of the game"},
    "description": {"type": "string", "description": "Full detailed description of the game"},
    "game_url": {"type": "string", "format": "uri", "description": "URL to the game's official page on the platform"},
    "genre": {"type": "string", "description": "Genre of the game (e.g., Shooter, RPG)"},
    "platform": {"type": "string", "description": "Supported platform (e.g., Windows, Browser)"},
    "publisher": {"type": "string", "description": "Publisher of the game"},
    "developer": {"type": "string", "description": "Developer of the game"},
    "release_date": {"type": "string", "format": "date", "description": "Release date of the game (YYYY-MM-DD)"},
    "freetogame_profile_url": {"type": "string", "format": "uri", "description": "URL to the game's profile on FreeToGame"},
    "minimum_system_requirements": {
      "type": "object",
      "description": "Minimum system requirements to run the game",
      "properties": {
        "os": {"type": "string", "description": "Required operating system"},
        "processor": {"type": "string", "description": "Required processor"},
        "memory": {"type": "string", "description": "Required RAM"},
        "graphics": {"type": "string", "description": "Required graphics card"},
        "storage": {"type": "string", "description": "Required storage space"}
      },
      "required": ["os", "processor", "memory", "graphics", "storage"]
    },
    "screenshots": {
      "type": "array",
      "description": "List of screenshots for the game",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "integer", "description": "Unique identifier for the screenshot"},
          "image": {"type": "string", "format": "uri", "description": "URL to the screenshot image"}
        },
        "required": ["id", "image"]
      }
    }
  },
  "required": [
    "id", "title", "thumbnail", "status", "short_description", "description",
    "game_url", "genre", "platform", "publisher", "developer", "release_date",
    "freetogame_profile_url", "minimum_system_requirements", "screenshots"
  ]
}
```
    """
    url = "https://free-to-play-games-database.p.rapidapi.com/api/game"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": game_id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-to-play-games-database.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

