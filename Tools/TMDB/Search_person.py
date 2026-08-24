import os
import requests


def Search_person(query):
    """
    :API_description: Search for people by their name and also known as names.
    :param query: Search for people by their name and also known as names.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "Current page number"
        },
        "results": {
          "type": "array",
          "description": "List of person results",
          "items": {
            "$ref": "#/$defs/Person"
          }
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages"
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results"
        }
      },
      "required": [
        "page",
        "results",
        "total_pages",
        "total_results"
      ],
      "$defs": {
        "Person": {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "gender": {
              "type": "integer",
              "description": "Gender: 0=not set, 1=female, 2=male"
            },
            "id": {
              "type": "integer"
            },
            "known_for_department": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "original_name": {
              "type": "string"
            },
            "popularity": {
              "type": "number"
            },
            "profile_path": {
              "type": [
                "string",
                "null"
              ],
              "description": "Path to profile image, can be null"
            },
            "known_for": {
              "type": "array",
              "description": "List of known works (movies or TV shows)",
              "items": {
                "$ref": "#/$defs/KnownFor"
              }
            }
          },
          "required": [
            "adult",
            "gender",
            "id",
            "known_for_department",
            "name",
            "original_name",
            "popularity",
            "known_for"
          ]
        },
        "KnownFor": {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": [
                "string",
                "null"
              ]
            },
            "id": {
              "type": "integer"
            },
            "title": {
              "type": "string",
              "description": "Title of the movie (for TV shows, name may be used)"
            },
            "original_language": {
              "type": "string"
            },
            "original_title": {
              "type": "string",
              "description": "Original title"
            },
            "overview": {
              "type": "string"
            },
            "poster_path": {
              "type": [
                "string",
                "null"
              ]
            },
            "media_type": {
              "type": "string",
              "description": "Type of media: 'movie' or 'tv'"
            },
            "genre_ids": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "popularity": {
              "type": "number"
            },
            "release_date": {
              "type": "string",
              "description": "Release date in YYYY-MM-DD format"
            },
            "video": {
              "type": "boolean"
            },
            "vote_average": {
              "type": "number"
            },
            "vote_count": {
              "type": "integer"
            }
          },
          "required": [
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        }
      }
    }
    ```
    """
    if query is None:
        raise ValueError("`query` is required.")

    url = "https://api.themoviedb.org/3/search/person"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    if not bearer_token:
        raise Exception("TMDB_BEARER_TOKEN is not set.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = {}
    params["query"] = query

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
