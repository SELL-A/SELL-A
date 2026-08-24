import os
import requests

def Anime(page=None, pageSize=None):
    """
    :API_description: Retrieve a list of anime with detailed information including ID, name, status, and episodes.
    :param page: The page number to retrieve (default: 1).
    :param pageSize: The number of items per page (default: 10).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "animeId": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "alternativeNames": {
            "type": "object",
            "properties": {
              "synonyms": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "japanese": {
                "type": "string"
              },
              "english": {
                "type": "string"
              }
            }
          },
          "slug": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "background": {
            "type": ["string", "null"]
          },
          "image": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "locale": {
            "type": "string"
          },
          "episodes": {
            "type": "string"
          },
          "aired": {
            "type": "string"
          },
          "premiered": {
            "type": "string"
          },
          "broadcast": {
            "type": "string"
          },
          "licensors": {
            "type": "string"
          },
          "studios": {
            "type": "string"
          },
          "demographic": {
            "type": "string"
          },
          "duration": {
            "type": "string"
          },
          "rating": {
            "type": "string"
          },
          "related": {
            "type": "object",
            "properties": {
              "adaptation": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "prequel": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "sequel": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "side_story": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "other": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "parent_story": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "alternative_version": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "alternative_setting": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "totalItems": {
          "type": "integer"
        },
        "itemCount": {
          "type": "integer"
        },
        "itemsPerPage": {
          "type": "integer"
        },
        "totalPages": {
          "type": "integer"
        },
        "currentPage": {
          "type": "integer"
        }
      }
    }
  }
}
```
    """
    url = "https://anime-manga-and-novels-api.p.rapidapi.com/anime"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"page": page, "pageSize": pageSize}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-manga-and-novels-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    print(Anime(1, 10))