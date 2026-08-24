import os
import requests

def Get_One_Anime_By_Ranking(ranking_id):
    """
    :API_description: Retrieve detailed information about a specific anime based on its ranking.
    :param ranking_id: The ID of the ranking to retrieve anime information for.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "_id": {
      "type": "string",
      "description": "Unique identifier for the anime."
    },
    "title": {
      "type": "string",
      "description": "Primary title of the anime."
    },
    "alternativeTitles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of alternative titles for the anime."
    },
    "ranking": {
      "type": "integer",
      "description": "Ranking of the anime."
    },
    "genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of genres associated with the anime."
    },
    "episodes": {
      "type": "integer",
      "description": "Number of episodes in the anime."
    },
    "hasEpisode": {
      "type": "boolean",
      "description": "Indicates if the anime has episodes."
    },
    "hasRanking": {
      "type": "boolean",
      "description": "Indicates if the anime has a ranking."
    },
    "image": {
      "type": "string",
      "description": "URL to the main image of the anime."
    },
    "link": {
      "type": "string",
      "description": "URL to the anime's page."
    },
    "status": {
      "type": "string",
      "description": "Current airing status of the anime."
    },
    "synopsis": {
      "type": "string",
      "description": "Detailed description of the anime's plot."
    },
    "thumb": {
      "type": "string",
      "description": "URL to the thumbnail image of the anime."
    },
    "type": {
      "type": "string",
      "description": "Type of the anime (e.g., TV, movie)."
    }
  },
  "required": ["_id", "title", "alternativeTitles", "ranking", "genres", "episodes", "hasEpisode", "hasRanking", "image", "link", "status", "synopsis", "thumb", "type"]
}
```
    """
    url = f"https://anime-db.p.rapidapi.com/anime/by-ranking/{ranking_id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-db.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")