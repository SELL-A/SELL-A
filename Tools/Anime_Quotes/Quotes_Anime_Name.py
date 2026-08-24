import os
import requests

def Quotes_Anime_Name(anime):
    """
    :API_description: Retrieve quotes, character details, and anime information from 'Naruto'.
    :param anime: The name of the anime for which the quote is requested.
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "description": "Unique identifier for the quote."
      },
      "anime": {
        "type": "string",
        "description": "Name of the anime associated with the quote. Currently always 'None'."
      },
      "character": {
        "type": "string",
        "description": "Name of the character who said the quote."
      },
      "quote": {
        "type": "string",
        "description": "The actual quote said by the character."
      },
      "thumbnail_url": {
        "type": "string",
        "description": "URL to the thumbnail image of the anime."
      },
      "character_thumbnail_url": {
        "type": "string",
        "description": "URL to the thumbnail image of the character."
      },
      "score": {
        "type": "string",
        "description": "Score or rating associated with the quote."
      },
      "synopsis": {
        "type": "string",
        "description": "Synopsis or summary of the anime."
      }
    },
    "required": ["id", "anime", "character", "quote", "thumbnail_url", "character_thumbnail_url", "score", "synopsis"]
  }
}
```
    """
    url = f"https://anime-quotes5.p.rapidapi.com/anime-quotes/{quote(str(anime))}"
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