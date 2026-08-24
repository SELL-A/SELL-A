import os
import requests

def Filter_games_by_multiple_tags(tag: str, platform: str):
    """
    :API_description: Retrieve a list of free-to-play games filtered by multiple tags and optionally by platform.
    :param tag: The tag used to filter games (e.g., "3d.mmorpg.fantasy.pvp").
    :param platform: The platform for which games are filtered (e.g., "pc").
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "integer",
        "description": "Unique identifier for the game."
      },
      "title": {
        "type": "string",
        "description": "Title of the game."
      },
      "thumbnail": {
        "type": "string",
        "description": "URL to the thumbnail image of the game."
      },
      "short_description": {
        "type": "string",
        "description": "Brief description of the game."
      },
      "game_url": {
        "type": "string",
        "description": "URL to the game's main page."
      },
      "genre": {
        "type": "string",
        "description": "Genre of the game."
      },
      "platform": {
        "type": "string",
        "description": "Platform on which the game is available."
      },
      "publisher": {
        "type": "string",
        "description": "Publisher of the game."
      },
      "developer": {
        "type": "string",
        "description": "Developer of the game."
      },
      "release_date": {
        "type": "string",
        "description": "Release date of the game in YYYY-MM-DD format."
      },
      "freetogame_profile_url": {
        "type": "string",
        "description": "URL to the game's profile on the FreeToGame website."
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
    url = "https://free-to-play-games-database.p.rapidapi.com/api/filter"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"tag": tag, "platform": platform}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-to-play-games-database.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

