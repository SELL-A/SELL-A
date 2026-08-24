import os
import requests

def Games_by_platform_and_category_and_sorted(platform: str, category: str, sort_by: str):
    """
    :API_description: Retrieve a list of free-to-play games filtered by platform, category, and sorted by a specified criterion.
    :param platform: The gaming platform (e.g., "browser", "pc").
    :param category: The game category (e.g., "mmorpg", "shooter").
    :param sort_by: The sorting criteria (e.g., "release-date", "popularity").
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
        "description": "URL to the game's main page or download link."
      },
      "genre": {
        "type": "string",
        "description": "Genre of the game."
      },
      "platform": {
        "type": "string",
        "description": "Platform(s) on which the game can be played."
      },
      "publisher": {
        "type": "string",
        "description": "Company that published the game."
      },
      "developer": {
        "type": "string",
        "description": "Company that developed the game."
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
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"platform": platform, "category": category, "sort-by": sort_by}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-to-play-games-database.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")