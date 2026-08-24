import os
import requests

def Get_All(page, size, search, genres=None, sortBy=None, sortOrder=None):
    """
    :API_description: Retrieve detailed information about anime titles, including identifiers, titles, rankings, genres, and more, with pagination support.
    :param page: The page number of the results to retrieve.
    :param size: The number of results per page.
    :param search: The search term to filter anime titles .
    :param genres: A comma-separated list of genres to filter the anime (optional).
    :param sortBy: The field to sort the results by, e.g., ranking (optional).
    :param sortOrder: The order of sorting, either 'asc' for ascending or 'desc' for descending (optional).
    :response_schema: 
    ```json
    {
      "data": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "_id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alternativeTitles": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "ranking": {
              "type": "integer"
            },
            "genres": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "episodes": {
              "type": "integer"
            },
            "hasEpisode": {
              "type": "boolean"
            },
            "hasRanking": {
              "type": "boolean"
            },
            "image": {
              "type": "string"
            },
            "link": {
              "type": "string"
            },
            "status": {
              "type": "string"
            },
            "synopsis": {
              "type": "string"
            },
            "thumb": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          },
          "required": [
            "_id",
            "title",
            "alternativeTitles",
            "ranking",
            "genres",
            "episodes",
            "hasEpisode",
            "hasRanking",
            "image",
            "link",
            "status",
            "synopsis",
            "thumb",
            "type"
          ]
        }
      },
      "meta": {
        "type": "object",
        "properties": {
          "page": {
            "type": "integer"
          },
          "size": {
            "type": "integer"
          },
          "totalData": {
            "type": "integer"
          },
          "totalPage": {
            "type": "integer"
          }
        },
        "required": [
          "page",
          "size",
          "totalData",
          "totalPage"
        ]
      }
    }
    ```
    """
    url = "https://anime-db.p.rapidapi.com/anime"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "page": page,
        "size": size,
        "search": search,
        "genres": genres,
        "sortBy": sortBy,
        "sortOrder": sortOrder
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-db.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

