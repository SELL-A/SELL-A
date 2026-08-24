import os
import requests


def Get_popular_tv():
    """
    :API_description: Get a list of TV shows ordered by popularity.
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
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Backdrop image path"
              },
              "first_air_date": {
                "type": "string",
                "description": "First air date"
              },
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "description": "Genre IDs"
              },
              "id": {
                "type": "integer",
                "description": "TV show ID"
              },
              "name": {
                "type": "string",
                "description": "TV show name"
              },
              "origin_country": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "Origin country codes"
              },
              "original_language": {
                "type": "string",
                "description": "Original language code"
              },
              "original_name": {
                "type": "string",
                "description": "Original name"
              },
              "overview": {
                "type": "string",
                "description": "Overview or description"
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score"
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Poster image path"
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote score"
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes"
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
      ]
    }
    ```
    """

    url = "https://api.themoviedb.org/3/tv/popular"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
