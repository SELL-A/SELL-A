import os
import requests

def Get_artists(ids):
    """
    :API_description: Retrieve detailed information about a Spotify artists.
    :param ids: string or list of artist IDs (comma separated)
    :response_schema:
    ```
JSON_schema:
{
  "type": "object",
  "properties": {
    "artists": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "external_urls": {
            "type": "object",
            "properties": {
              "spotify": {
                "type": "string",
                "description": "URL to the artist's Spotify profile"
              }
            },
            "required": ["spotify"],
            "description": "External URLs for the artist, keyed by service name"
          },
          "followers": {
            "type": "object",
            "properties": {
              "href": {
                "type": ["string", "null"],
                "description": "URL to the followers endpoint (nullable)"
              },
              "total": {
                "type": "integer",
                "description": "Total number of followers"
              }
            },
            "required": ["href", "total"],
            "description": "Follower count information"
          },
          "genres": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of genre names associated with the artist"
          },
          "href": {
            "type": "string",
            "description": "API endpoint URL for this specific artist resource"
          },
          "id": {
            "type": "string",
            "description": "Spotify unique identifier for the artist"
          },
          "images": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "url": {
                  "type": "string",
                  "description": "Image URL"
                },
                "height": {
                  "type": "integer",
                  "description": "Image height in pixels"
                },
                "width": {
                  "type": "integer",
                  "description": "Image width in pixels"
                }
              },
              "required": ["url", "height", "width"],
              "description": "Artist image metadata with different resolutions"
            },
            "description": "Array of artist images in various sizes"
          },
          "name": {
            "type": "string",
            "description": "Artist name"
          },
          "popularity": {
            "type": "integer",
            "minimum": 0,
            "maximum": 100,
            "description": "Popularity score from 0 to 100"
          },
          "type": {
            "type": "string",
            "enum": ["artist"],
            "description": "Resource type identifier"
          },
          "uri": {
            "type": "string",
            "description": "Spotify URI for the artist"
          }
        },
        "required": ["external_urls", "followers", "genres", "href", "id", "images", "name", "popularity", "type", "uri"],
        "description": "Artist object containing comprehensive metadata"
      },
      "description": "Array of artist objects returned by the API"
    }
  },
  "required": ["artists"],
  "description": "Root object containing artist search/retrieval results"
}
```
    """
    rapid_api_key = os.getenv('RAPID_API_KEY')
    url = "https://spotify81.p.rapidapi.com/artists"
    querystring = {"ids": ids}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "spotify81.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")