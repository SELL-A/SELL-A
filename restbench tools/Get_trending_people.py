import os
import requests


def Get_trending_people(time_window):
    """
    :API_description: Get the trending people on TMDB.
    :param time_window: The time window for the trending results. Allowed values: day, week.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer"
        },
        "results": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Person"
          }
        },
        "total_pages": {
          "type": "integer"
        },
        "total_results": {
          "type": "integer"
        }
      },
      "required": [
        "page",
        "results",
        "total_pages",
        "total_results"
      ],
      "definitions": {
        "Person": {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "original_name": {
              "type": "string"
            },
            "media_type": {
              "type": "string",
              "description": "Always 'person' in this context"
            },
            "popularity": {
              "type": "number"
            },
            "gender": {
              "type": "integer",
              "description": "0: not specified, 1: female, 2: male, 3: non-binary"
            },
            "known_for_department": {
              "type": "string"
            },
            "profile_path": {
              "type": [
                "string",
                "null"
              ],
              "description": "Path to profile image"
            },
            "known_for": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/MediaItem"
              }
            }
          },
          "required": [
            "adult",
            "id",
            "name",
            "original_name",
            "media_type",
            "popularity",
            "gender",
            "known_for_department",
            "profile_path",
            "known_for"
          ]
        },
        "MediaItem": {
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
              "description": "Present for movie media_type"
            },
            "original_language": {
              "type": "string"
            },
            "original_title": {
              "type": "string",
              "description": "Present for movie media_type"
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
              "enum": [
                "movie",
                "tv"
              ],
              "description": "Indicates whether item is a movie or TV show"
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
              "description": "Present for movie media_type (format: YYYY-MM-DD)"
            },
            "video": {
              "type": "boolean",
              "description": "Present for movie media_type"
            },
            "vote_average": {
              "type": "number"
            },
            "vote_count": {
              "type": "integer"
            },
            "name": {
              "type": "string",
              "description": "Present for tv media_type"
            },
            "original_name": {
              "type": "string",
              "description": "Present for tv media_type"
            },
            "first_air_date": {
              "type": "string",
              "description": "Present for tv media_type (format: YYYY-MM-DD)"
            },
            "origin_country": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Present for tv media_type"
            }
          },
          "required": [
            "adult",
            "id",
            "backdrop_path",
            "original_language",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "vote_average",
            "vote_count"
          ]
        }
      }
    }
    ```
    """
    if time_window is None:
        raise ValueError("`time_window` is required.")

    url = f"https://api.themoviedb.org/3/trending/person/{time_window}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
