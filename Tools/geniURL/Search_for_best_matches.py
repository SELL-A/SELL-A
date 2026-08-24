import os
import requests

def Search_for_best_matches(q, artist, song, format="json"):
    """
    :API_description: This endpoint searches for the best song matches based on a query or specific artist and song parameters.
    :param q: The search query, typically the song title.
    :param artist: The name of the artist.
    :param song: The name of the song.
    :param format: The format of the response, default is 'json'.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "boolean",
      "description": "Indicates whether an error occurred during the API call."
    },
    "matches": {
      "type": "integer",
      "description": "Number of matches found in the response."
    },
    "top": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string",
          "description": "URL to the top result."
        },
        "path": {
          "type": "string",
          "description": "Path to the top result."
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
              "description": "Name of the artist(s)."
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
                  "description": "URL to the primary artist's page."
                },
                "headerImage": {
                  "type": "string",
                  "description": "URL to the header image of the primary artist."
                },
                "image": {
                  "type": "string",
                  "description": "URL to the image of the primary artist."
                }
              }
            },
            "featuredArtists": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "List of featured artists."
            },
            "releaseDate": {
              "type": "object",
              "properties": {
                "year": {
                  "type": "integer",
                  "description": "Year of release."
                },
                "month": {
                  "type": "integer",
                  "description": "Month of release."
                },
                "day": {
                  "type": "integer",
                  "description": "Day of release."
                }
              }
            }
          }
        },
        "resources": {
          "type": "object",
          "properties": {
            "thumbnail": {
              "type": "string",
              "description": "URL to the thumbnail image."
            },
            "image": {
              "type": "string",
              "description": "URL to the full-size image."
            }
          }
        },
        "lyricsState": {
          "type": "string",
          "description": "State of the lyrics (e.g., 'complete')."
        },
        "id": {
          "type": "integer",
          "description": "Unique identifier for the song."
        }
      }
    },
    "all": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "description": "URL to the result."
          },
          "path": {
            "type": "string",
            "description": "Path to the result."
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
                "description": "Name of the artist(s)."
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
                    "description": "URL to the primary artist's page."
                  },
                  "headerImage": {
                    "type": "string",
                    "description": "URL to the header image of the primary artist."
                  },
                  "image": {
                    "type": "string",
                    "description": "URL to the image of the primary artist."
                  }
                }
              },
              "featuredArtists": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "List of featured artists."
              },
              "releaseDate": {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "integer",
                    "description": "Year of release."
                  },
                  "month": {
                    "type": "integer",
                    "description": "Month of release."
                  },
                  "day": {
                    "type": "integer",
                    "description": "Day of release."
                  }
                }
              }
            }
          },
          "resources": {
            "type": "object",
            "properties": {
              "thumbnail": {
                "type": "string",
                "description": "URL to the thumbnail image."
              },
              "image": {
                "type": "string",
                "description": "URL to the full-size image."
              }
            }
          },
          "lyricsState": {
            "type": "string",
            "description": "State of the lyrics (e.g., 'complete')."
          },
          "id": {
            "type": "integer",
            "description": "Unique identifier for the song."
          }
        }
      },
      "description": "List of all matching results."
    }
  }
}
```
    """
    url = "https://geniurl.p.rapidapi.com/search"
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

