import os
import requests

def Get_playlist(id):
    """
    :API_description: Retrieve detailed information about a Spotify playlist, including its name, owner, tracks, and images.
    :param id: The unique identifier for the Spotify playlist(e.g., "3IBcauSj5M2A6lTeffJzdv").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the playlist."
    },
    "owner": {
      "type": "object",
      "properties": {
        "display_name": {
          "type": "string",
          "description": "The display name of the playlist owner."
        },
        "uri": {
          "type": "string",
          "description": "The URI of the playlist owner."
        },
        "id": {
          "type": "string",
          "description": "The ID of the playlist owner."
        }
      },
      "description": "Information about the owner of the playlist."
    },
    "uri": {
      "type": "string",
      "description": "The URI of the playlist."
    },
    "public": {
      "type": "boolean",
      "description": "Indicates if the playlist is public."
    },
    "collaborative": {
      "type": "boolean",
      "description": "Indicates if the playlist is collaborative."
    },
    "followers": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "The total number of followers."
        }
      },
      "description": "Information about the followers of the playlist."
    },
    "tracks": {
      "type": "object",
      "properties": {
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "track": {
                "type": "object",
                "properties": {
                  "duration_ms": {
                    "type": "integer",
                    "description": "The duration of the track in milliseconds."
                  },
                  "type": {
                    "type": "string",
                    "description": "The type of the track."
                  }
                },
                "description": "Information about the track."
              }
            }
          },
          "description": "List of tracks in the playlist."
        },
        "total": {
          "type": "integer",
          "description": "The total number of tracks in the playlist."
        }
      },
      "description": "Information about the tracks in the playlist."
    },
    "images": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "description": "The URL of the image."
          },
          "height": {
            "type": ["integer", "null"],
            "description": "The height of the image."
          },
          "width": {
            "type": ["integer", "null"],
            "description": "The width of the image."
          }
        },
        "description": "Information about the images associated with the playlist."
      },
      "description": "List of images associated with the playlist."
    },
    "description": {
      "type": "string",
      "description": "The description of the playlist."
    }
  },
  "required": ["name", "owner", "uri", "public", "collaborative", "followers", "tracks", "images", "description"]
}
```
    """
    url = "https://spotify81.p.rapidapi.com/playlist/"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "spotify81.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")