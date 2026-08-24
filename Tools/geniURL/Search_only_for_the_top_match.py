import os
import requests

def Search_only_for_the_top_match(q, artist, song, format):
    """
    :API_description: This endpoint retrieves detailed information about the top matching song, including title, artist, release date, and lyrics availability.
    :param q: The query string to search for.
    :param artist: The name of the artist.
    :param song: The name of the song.
    :param format: The format of the response, e.g., 'json'.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "boolean",
      "description": "Indicates if there was an error in the API response."
    },
    "matches": {
      "type": "integer",
      "description": "Number of matches found for the query."
    },
    "url": {
      "type": "string",
      "format": "uri",
      "description": "URL to the lyrics page on Genius."
    },
    "path": {
      "type": "string",
      "description": "Path to the lyrics page on Genius."
    },
    "meta": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "Title of the song."
        },
        "fullTitle": {
          "type": "string",
          "description": "Full title of the song including the artist."
        },
        "artists": {
          "type": "string",
          "description": "Name of the artist(s) of the song."
        },
        "primaryArtist": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "Name of the primary artist."
            },
            "url": {
              "type": "string",
              "format": "uri",
              "description": "URL to the primary artist's page on Genius."
            },
            "headerImage": {
              "type": "string",
              "format": "uri",
              "description": "URL to the header image of the primary artist."
            },
            "image": {
              "type": "string",
              "format": "uri",
              "description": "URL to the image of the primary artist."
            }
          },
          "description": "Details about the primary artist of the song."
        },
        "featuredArtists": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of featured artists in the song."
        },
        "releaseDate": {
          "type": "object",
          "properties": {
            "year": {
              "type": "integer",
              "description": "Year of the song's release."
            },
            "month": {
              "type": "integer",
              "description": "Month of the song's release."
            },
            "day": {
              "type": "integer",
              "description": "Day of the song's release."
            }
          },
          "description": "Release date of the song."
        }
      },
      "description": "Metadata about the song."
    },
    "resources": {
      "type": "object",
      "properties": {
        "thumbnail": {
          "type": "string",
          "format": "uri",
          "description": "URL to the thumbnail image of the song."
        },
        "image": {
          "type": "string",
          "format": "uri",
          "description": "URL to the full-size image of the song."
        }
      },
      "description": "Resources related to the song, such as images."
    },
    "lyricsState": {
      "type": "string",
      "description": "State of the lyrics availability (e.g., 'complete')."
    },
    "id": {
      "type": "integer",
      "description": "Unique identifier for the song on Genius."
    }
  },
  "required": ["error", "matches", "url", "path", "meta", "resources", "lyricsState", "id"]
}
```
    """
    url = "https://geniurl.p.rapidapi.com/search/top"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"q": q, "artist": artist, "song": song, "format": format}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "geniurl.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

