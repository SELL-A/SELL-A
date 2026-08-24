import os
import requests

def Get_Games_list():
    """
    :API_description: Get a list of all free-to-play games.
    :param None
    :response_schema: 
    _summary should be concise._summary```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {"type": "integer"},
      "title": {"type": "string"},
      "thumbnail": {"type": "string", "format": "uri"},
      "short_description": {"type": "string"},
      "game_url": {"type": "string", "format": "uri"},
      "genre": {"type": "string"},
      "platform": {"type": "string"},
      "publisher": {"type": "string"},
      "developer": {"type": "string"},
      "release_date": {"type": "string", "format": "date"},
      "freetogame_profile_url": {"type": "string", "format": "uri"}
    },
    "required": ["id", "title", "thumbnail", "short_description", "game_url", "genre", "platform", "publisher", "developer", "release_date", "freetogame_profile_url"]
  }
}
```
    """
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-to-play-games-database.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")