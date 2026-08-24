import os
import requests

def Get_Games_by_category_or_tag(category):
    """
    :API_description: Get a list of games filtered by category or tag (e.g., MMORPG, shooter, strategy).
    :param category: The category of games to filter by (eg: "mmorpg", "shooter", "pvp", "mmofps" and "more").
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "integer",
        "description": "Unique identifier for the game"
      },
      "title": {
        "type": "string",
        "description": "Name of the game"
      },
      "thumbnail": {
        "type": "string",
        "description": "URL to the game's thumbnail image"
      },
      "short_description": {
        "type": "string",
        "description": "Brief description of the game"
      },
      "game_url": {
        "type": "string",
        "description": "URL to the game's page on the platform"
      },
      "genre": {
        "type": "string",
        "description": "Genre of the game (e.g., Shooter, MOBA)"
      },
      "platform": {
        "type": "string",
        "description": "Platform(s) the game is available on"
      },
      "publisher": {
        "type": "string",
        "description": "Publisher of the game"
      },
      "developer": {
        "type": "string",
        "description": "Developer of the game"
      },
      "release_date": {
        "type": "string",
        "description": "Release date of the game (format: YYYY-MM-DD)"
      },
      "freetogame_profile_url": {
        "type": "string",
        "description": "URL to the game's profile on freetogame.com"
      }
    },
    "required": [
      "id",
      "title",
      "thumbnail",
      "short_description",
      "game_url",
      "genre",
      "platform",
      "publisher",
      "developer",
      "release_date",
      "freetogame_profile_url"
    ]
  }
}
```
    """
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"category": category}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-to-play-games-database.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

