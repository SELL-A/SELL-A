import os
import requests


def Search_movie(query):
    """
    :API_description: Search for movies.
    :param query: Search for movies.
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
                "description": "Path to backdrop image or null"
              },
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "description": "Array of genre IDs"
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
                ]
              },
              "release_date": {
                "type": "string",
                "description": "Release date in YYYY-MM-DD format or empty string"
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
    if query is None:
        raise ValueError("`query` is required.")

    url = "https://api.themoviedb.org/3/search/movie"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    params = {"query": query}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
