import os
import requests


def Get_top_rated_movies(region=None):
    """
    :API_description: Get a list of movies ordered by rating.
    :param region: ISO-3166-1 code
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
                ],
                "description": "Path to backdrop image, may be null"
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
              "original_language": {
                "type": "string"
              },
              "original_title": {
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
                ],
                "description": "Path to poster image, may be null"
              },
              "release_date": {
                "type": "string"
              },
              "title": {
                "type": "string"
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
              "genre_ids",
              "id",
              "original_language",
              "original_title",
              "overview",
              "popularity",
              "poster_path",
              "release_date",
              "title",
              "video",
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

    url = "https://api.themoviedb.org/3/movie/top_rated"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = {"region":region}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
