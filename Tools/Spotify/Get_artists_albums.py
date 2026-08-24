import os
import requests

def Get_artists_albums(id):
    """
    :API_description: Retrieve detailed information about a albums of Spotify artists
    :param id: The Spotify artist ID (e.g., "3IBcauSj5M2A6lTeffJzdv").
    :response_schema: 
    ```JSON_schema
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "artist": {
          "type": "object",
          "properties": {
            "discography": {
              "type": "object",
              "properties": {
                "albums": {
                  "type": "object",
                  "properties": {
                    "totalCount": {
                      "type": "integer",
                      "description": "The total number of album items/groups returned."
                    },
                    "items": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "releases": {
                            "type": "object",
                            "properties": {
                              "items": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "string",
                                      "description": "Unique identifier for the album (e.g., Spotify ID)."
                                    },
                                    "uri": {
                                      "type": "string",
                                      "description": "Spotify URI for the album."
                                    },
                                    "name": {
                                      "type": "string",
                                      "description": "Name of the album."
                                    },
                                    "type": {
                                      "type": "string",
                                      "description": "Release type (e.g., 'ALBUM')."
                                    },
                                    "date": {
                                      "type": "object",
                                      "properties": {
                                        "year": {
                                          "type": "integer",
                                          "description": "Release year."
                                        },
                                        "isoString": {
                                          "type": "string",
                                          "description": "Full release date in ISO 8601 format."
                                        }
                                      },
                                      "required": ["year", "isoString"]
                                    },
                                    "coverArt": {
                                      "type": "object",
                                      "properties": {
                                        "sources": {
                                          "type": "array",
                                          "items": {
                                            "type": "object",
                                            "properties": {
                                              "url": {
                                                "type": "string",
                                                "description": "URL of the cover art image."
                                              },
                                              "width": {
                                                "type": "integer",
                                                "description": "Width of the image in pixels."
                                              },
                                              "height": {
                                                "type": "integer",
                                                "description": "Height of the image in pixels."
                                              }
                                            },
                                            "required": ["url", "width", "height"]
                                          },
                                          "description": "Array of image sources in different resolutions."
                                        }
                                      },
                                      "required": ["sources"]
                                    },
                                    "playability": {
                                      "type": "object",
                                      "properties": {
                                        "playable": {
                                          "type": "boolean",
                                          "description": "Indicates if the album is playable."
                                        },
                                        "reason": {
                                          "type": "string",
                                          "description": "Reason for playability status (e.g., 'PLAYABLE')."
                                        }
                                      },
                                      "required": ["playable", "reason"]
                                    },
                                    "sharingInfo": {
                                      "type": "object",
                                      "properties": {
                                        "shareId": {
                                          "type": "string",
                                          "description": "Unique ID for sharing the album."
                                        },
                                        "shareUrl": {
                                          "type": "string",
                                          "description": "Full URL for sharing the album on Spotify."
                                        }
                                      },
                                      "required": ["shareId", "shareUrl"]
                                    },
                                    "tracks": {
                                      "type": "object",
                                      "properties": {
                                        "totalCount": {
                                          "type": "integer",
                                          "description": "Total number of tracks on the album."
                                        }
                                      },
                                      "required": ["totalCount"]
                                    }
                                  },
                                  "required": ["id", "uri", "name", "type", "date", "coverArt", "playability", "sharingInfo", "tracks"]
                                },
                                "description": "List of album releases (can include multiple versions like standard/deluxe)."
                              }
                            },
                            "required": ["items"]
                          }
                        },
                        "required": ["releases"]
                      },
                      "description": "Array of objects, each containing a 'releases' object with an array of album items."
                    }
                  },
                  "required": ["totalCount", "items"]
                }
              },
              "required": ["albums"]
            }
          },
          "required": ["discography"]
        }
      },
      "required": ["artist"]
    }
  },
  "required": ["data"],
  "description": "Schema representing the discography albums of an artist, typically from a music streaming service API."
}
```
    """
    url = "https://spotify81.p.rapidapi.com/artist_albums"
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