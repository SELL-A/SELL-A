import os
import requests

def Get_Manga_By_Id(manga_id):
    """
    :API_description: Retrieve detailed information about a specific manga, including its title, status, and related metadata.
    :param manga_id: The ID of the manga to retrieve details for.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "mangaId": {
      "type": "integer",
      "description": "Unique identifier for the manga."
    },
    "name": {
      "type": "string",
      "description": "The title of the manga."
    },
    "slug": {
      "type": "string",
      "description": "A URL-friendly version of the manga title."
    },
    "alternativeNames": {
      "type": "object",
      "properties": {
        "japanese": {
          "type": "string",
          "description": "Alternative Japanese title of the manga."
        }
      },
      "description": "Alternative names for the manga, typically in different languages."
    },
    "description": {
      "type": "string",
      "description": "A brief description or summary of the manga."
    },
    "status": {
      "type": "string",
      "description": "The current status of the manga (e.g., 'Finished', 'Ongoing')."
    },
    "locale": {
      "type": "string",
      "description": "The locale or language setting for the manga information."
    },
    "volumes": {
      "type": "integer",
      "description": "The number of volumes the manga has."
    },
    "chapters": {
      "type": "integer",
      "description": "The number of chapters the manga has."
    },
    "published": {
      "type": "string",
      "description": "The month and year when the manga was first published."
    },
    "demographic": {
      "type": "string",
      "description": "The target demographic for the manga (e.g., 'Shounen', 'Seinen')."
    },
    "related": {
      "type": "object",
      "description": "Related manga or series, if any."
    }
  },
  "required": [
    "mangaId",
    "name",
    "slug",
    "alternativeNames",
    "description",
    "status",
    "locale",
    "volumes",
    "chapters",
    "published",
    "demographic",
    "related"
  ]
}
```
    """
    url = f"https://anime-manga-and-novels-api.p.rapidapi.com/manga/{manga_id}"
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