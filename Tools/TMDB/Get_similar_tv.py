import os
import requests


def Get_similar_tv(series_id):
    """
    :API_description: Get a list of similar TV shows.
    :param series_id: The ID of the TV series.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "Current page number."
        },
        "results": {
          "type": "array",
          "description": "List of similar TV shows.",
          "items": {
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
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                }
              },
              "id": {
                "type": "integer"
              },
              "origin_country": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "original_language": {
                "type": "string"
              },
              "original_name": {
                "type": "string"
              },
              "overview": {
                "type": "string"
              },
              "popularity": {
                "type": "number"
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "first_air_date": {
                "type": "string"
              },
              "name": {
                "type": "string"
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
              "genre_ids",
              "id",
              "origin_country",
              "original_language",
              "original_name",
              "overview",
              "popularity",
              "poster_path",
              "first_air_date",
              "name",
              "vote_average",
              "vote_count"
            ]
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
      ]
    }
    ```
    """
    if series_id is None:
        raise ValueError("`series_id` is required.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}/similar"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    if not bearer_token:
        raise Exception("TMDB_BEARER_TOKEN is not set.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = None

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
