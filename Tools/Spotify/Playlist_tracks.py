import os
import requests

def Playlist_tracks(id, offset=0, limit=100):
    """
    :API_description: Retrieve detailed metadata for tracks in a playlist, including track, album, and artist information, along with pagination details.
    :param id: The Spotify playlist ID.
    :param offset: The index of the first track to return (default is 0).
    :param limit: The maximum number of tracks to return (default is 100).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "limit": {
      "type": "integer",
      "description": "The maximum number of items to return."
    },
    "next": {
      "type": ["string", "null"],
      "description": "URL to the next set of items. Null if there are no more items."
    },
    "offset": {
      "type": "integer",
      "description": "The index of the first item to return."
    },
    "previous": {
      "type": ["string", "null"],
      "description": "URL to the previous set of items. Null if there are no previous items."
    },
    "total": {
      "type": "integer",
      "description": "The total number of items available."
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "added_at": {
            "type": "string",
            "format": "date-time",
            "description": "The date and time the track was added."
          },
          "primary_color": {
            "type": ["string", "null"],
            "description": "The primary color of the track's album art."
          },
          "video_thumbnail": {
            "type": "object",
            "properties": {
              "url": {
                "type": ["string", "null"],
                "description": "URL to the video thumbnail."
              }
            }
          },
          "is_local": {
            "type": "boolean",
            "description": "Indicates if the track is a local file."
          },
          "added_by": {
            "type": "object",
            "properties": {
              "external_urls": {
                "type": "object",
                "properties": {
                  "spotify": {
                    "type": "string",
                    "description": "URL to the user's Spotify profile."
                  }
                }
              },
              "id": {
                "type": "string",
                "description": "The user's Spotify ID."
              },
              "type": {
                "type": "string",
                "description": "The type of the user (e.g., 'user')."
              },
              "uri": {
                "type": "string",
                "description": "The Spotify URI for the user."
              }
            }
          },
          "track": {
            "type": "object",
            "properties": {
              "preview_url": {
                "type": ["string", "null"],
                "description": "URL to a 30-second preview of the track."
              },
              "is_playable": {
                "type": "boolean",
                "description": "Indicates if the track is playable."
              },
              "explicit": {
                "type": "boolean",
                "description": "Indicates if the track is explicit."
              },
              "type": {
                "type": "string",
                "description": "The type of the track (e.g., 'track')."
              },
              "episode": {
                "type": "boolean",
                "description": "Indicates if the track is an episode."
              },
              "track": {
                "type": "boolean",
                "description": "Indicates if the track is a track."
              },
              "album": {
                "type": "object",
                "properties": {
                  "is_playable": {
                    "type": "boolean",
                    "description": "Indicates if the album is playable."
                  },
                  "type": {
                    "type": "string",
                    "description": "The type of the album (e.g., 'album')."
                  },
                  "album_type": {
                    "type": "string",
                    "description": "The type of the album (e.g., 'single', 'album')."
                  },
                  "id": {
                    "type": "string",
                    "description": "The Spotify ID for the album."
                  },
                  "images": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "height": {
                          "type": "integer",
                          "description": "The height of the image."
                        },
                        "url": {
                          "type": "string",
                          "description": "URL to the image."
                        },
                        "width": {
                          "type": "integer",
                          "description": "The width of the image."
                        }
                      }
                    },
                    "description": "Array of images associated with the album."
                  },
                  "name": {
                    "type": "string",
                    "description": "The name of the album."
                  },
                  "release_date": {
                    "type": "string",
                    "format": "date",
                    "description": "The release date of the album."
                  },
                  "release_date_precision": {
                    "type": "string",
                    "description": "The precision of the release date (e.g., 'day')."
                  },
                  "uri": {
                    "type": "string",
                    "description": "The Spotify URI for the album."
                  },
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
                              "description": "URL to the artist's Spotify profile."
                            }
                          }
                        },
                        "id": {
                          "type": "string",
                          "description": "The artist's Spotify ID."
                        },
                        "name": {
                          "type": "string",
                          "description": "The name of the artist."
                        },
                        "type": {
                          "type": "string",
                          "description": "The type of the artist (e.g., 'artist')."
                        },
                        "uri": {
                          "type": "string",
                          "description": "The Spotify URI for the artist."
                        }
                      }
                    },
                    "description": "Array of artists associated with the album."
                  },
                  "external_urls": {
                    "type": "object",
                    "properties": {
                      "spotify": {
                        "type": "string",
                        "description": "URL to the album on Spotify."
                      }
                    }
                  },
                  "total_tracks": {
                    "type": "integer",
                    "description": "The total number of tracks in the album."
                  }
                }
              },
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
                          "description": "URL to the artist's Spotify profile."
                        }
                      }
                    },
                    "id": {
                      "type": "string",
                      "description": "The artist's Spotify ID."
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of the artist."
                    },
                    "type": {
                      "type": "string",
                      "description": "The type of the artist (e.g., 'artist')."
                    },
                    "uri": {
                      "type": "string",
                      "description": "The Spotify URI for the artist."
                    }
                  }
                },
                "description": "Array of artists associated with the track."
              },
              "disc_number": {
                "type": "integer",
                "description": "The disc number the track is on."
              },
              "track_number": {
                "type": "integer",
                "description": "The track number of the track."
              },
              "duration_ms": {
                "type": "integer",
                "description": "The duration of the track in milliseconds."
              },
              "external_ids": {
                "type": "object",
                "properties": {
                  "isrc": {
                    "type": "string",
                    "description": "The International Standard Recording Code (ISRC) for the track."
                  }
                }
              },
              "external_urls": {
                "type": "object",
                "properties": {
                  "spotify": {
                    "type": "string",
                    "description": "URL to the track on Spotify."
                  }
                }
              },
              "id": {
                "type": "string",
                "description": "The Spotify ID for the track."
              },
              "name": {
                "type": "string",
                "description": "The name of the track."
              },
              "popularity": {
                "type": "integer",
                "description": "The popularity of the track."
              },
              "uri": {
                "type": "string",
                "description": "The Spotify URI for the track."
              },
              "is_local": {
                "type": "boolean",
                "description": "Indicates if the track is a local file."
              }
            }
          }
        }
      },
      "description": "Array of items, each representing a track."
    }
  }
}
```
    """
    url = "https://spotify81.p.rapidapi.com/playlist_tracks/"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": id, "offset": offset, "limit": limit}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "spotify81.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
