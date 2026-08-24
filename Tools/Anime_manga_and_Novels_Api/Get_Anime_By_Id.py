import os
import requests

def Get_Anime_By_Id(anime_id):
    """
    :API_description: Retrieve comprehensive details about a specific anime, including its unique identifier, name, status, and related metadata.
    :param anime_id: The ID of the anime to retrieve details for.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "animeId": {
      "type": "integer",
      "description": "Unique identifier for the anime."
    },
    "name": {
      "type": "string",
      "description": "Name of the anime."
    },
    "alternativeNames": {
      "type": "object",
      "properties": {
        "synonyms": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of alternative names or synonyms for the anime."
        }
      },
      "description": "Object containing alternative names for the anime."
    },
    "slug": {
      "type": "string",
      "description": "URL-friendly version of the anime name."
    },
    "description": {
      "type": "string",
      "description": "Brief description of the anime."
    },
    "background": {
      "type": "string",
      "description": "Background information or story of the anime."
    },
    "image": {
      "type": "string",
      "description": "URL or path to the image representing the anime."
    },
    "status": {
      "type": "string",
      "description": "Current status of the anime (e.g., 'Finished Airing')."
    },
    "locale": {
      "type": "string",
      "description": "Locale setting for the anime data (e.g., 'en_US')."
    },
    "episodes": {
      "type": "string",
      "description": "Number of episodes in the anime."
    },
    "aired": {
      "type": "string",
      "description": "Dates when the anime was aired."
    },
    "premiered": {
      "type": "string",
      "description": "Season and year when the anime premiered."
    },
    "broadcast": {
      "type": "string",
      "description": "Broadcast details of the anime."
    },
    "licensors": {
      "type": "string",
      "description": "Licensors of the anime."
    },
    "studios": {
      "type": "string",
      "description": "Studios involved in producing the anime."
    },
    "demographic": {
      "type": "string",
      "description": "Target demographic for the anime."
    },
    "duration": {
      "type": "string",
      "description": "Duration of each episode."
    },
    "rating": {
      "type": "string",
      "description": "Content rating for the anime."
    },
    "related": {
      "type": "object",
      "properties": {
        "adaptation": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of related adaptations."
        },
        "prequel": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of related prequels."
        }
      },
      "description": "Object containing related anime titles."
    }
  },
  "required": [
    "animeId",
    "name",
    "alternativeNames",
    "slug",
    "description",
    "background",
    "image",
    "status",
    "locale",
    "episodes",
    "aired",
    "premiered",
    "broadcast",
    "licensors",
    "studios",
    "demographic",
    "duration",
    "rating",
    "related"
  ]
}
```
    """
    url = f"https://anime-manga-and-novels-api.p.rapidapi.com/anime/{anime_id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-manga-and-novels-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")