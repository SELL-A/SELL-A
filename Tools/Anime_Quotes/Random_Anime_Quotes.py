import os
import requests

def Random_Anime_Quotes():
    """
    :API_description: Retrieve detailed information about random anime characters, including quotes, anime titles, thumbnails, ratings, and synopses.
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "description": "Unique identifier for the record"
      },
      "character": {
        "type": "string",
        "description": "Name of the character"
      },
      "quote": {
        "type": "string",
        "description": "A quote said by the character"
      },
      "anime": {
        "type": "string",
        "description": "Name of the anime"
      },
      "thumbnail_url": {
        "type": "string",
        "format": "uri",
        "description": "URL to the thumbnail image of the anime"
      },
      "character_thumbnail_url": {
        "type": ["string", "null"],
        "format": "uri",
        "description": "URL to the thumbnail image of the character"
      },
      "score": {
        "type": "string",
        "description": "Score or rating associated with the anime"
      },
      "synopsis": {
        "type": "string",
        "description": "Synopsis or summary of the anime"
      }
    },
    "required": ["id", "character", "quote", "anime", "thumbnail_url", "character_thumbnail_url", "score", "synopsis"]
  }
}
```
    """
    url = "https://anime-quotes5.p.rapidapi.com/random&count=3"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-quotes5.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
