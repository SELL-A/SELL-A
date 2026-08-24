import os
import requests


def Get_on_the_air_tv():
    """
    :API_description: Get a list of TV shows that air in the next 7 days.
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
            "type": "object",
            "properties": {
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "first_air_date": {
                "type": "string"
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
              "name": {
                "type": "string"
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
              "vote_average": {
                "type": "number"
              },
              "vote_count": {
                "type": "integer"
              }
            },
            "required": [
              "backdrop_path",
              "first_air_date",
              "genre_ids",
              "id",
              "name",
              "origin_country",
              "original_language",
              "original_name",
              "overview",
              "popularity",
              "poster_path",
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

    url = "https://api.themoviedb.org/3/tv/on_the_air"
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
