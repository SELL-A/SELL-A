import os
import requests

def Get_Games_by_platform(platform):
    """
    :API_description: Get a list of games filtered by platform (e.g., PC, browser).
    :param platform: The platform for which to fetch the games (e.g., "pc", "browser" or "all").
    :response_schema: 
    ```JSON_schema
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": { "type": "integer", "description": "Unique identifier for the game" },
      "title": { "type": "string", "description": "Name of the game" },
      "thumbnail": { "type": "string", "format": "uri", "description": "URL to the game's thumbnail image" },
      "short_description": { "type": "string", "description": "Brief description of the game" },
      "game_url": { "type": "string", "format": "uri", "description": "URL to the game's page on the platform" },
      "genre": { "type": "string", "description": "Genre classification of the game" },
      "platform": { "type": "string", "description": "Supported platform(s)" },
      "publisher": { "type": "string", "description": "Publisher of the game" },
      "developer": { "type": "string", "description": "Developer of the game" },
      "release_date": { "type": "string", "format": "date", "description": "Release date in YYYY-MM-DD format" },
      "freetogame_profile_url": { "type": "string", "format": "uri", "description": "URL to the game's profile on FreeToGame" }
    },
    "required": ["id", "title", "thumbnail", "short_description", "game_url", "genre", "platform", "publisher", "developer", "release_date", "freetogame_profile_url"]
  }
}
    ```
    """
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"platform": platform}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-to-play-games-database.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

