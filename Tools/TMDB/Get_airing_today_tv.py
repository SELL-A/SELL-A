import os
import requests


def Get_airing_today_tv():
    """
    :API_description: Get a list of TV shows airing today.
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
                "description": "Backdrop image path, may be null"
              },
              "first_air_date": {
                "type": "string",
                "description": "First air date of the TV show"
              },
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "description": "Array of genre IDs associated with the show"
              },
              "id": {
                "type": "integer",
                "description": "Unique identifier for the TV show"
              },
              "name": {
                "type": "string",
                "description": "Name of the TV show"
              },
              "origin_country": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "Array of origin country codes"
              },
              "original_language": {
                "type": "string",
                "description": "Original language code (e.g., 'tl', 'hi', 'pt')"
              },
              "original_name": {
                "type": "string",
                "description": "Original name of the TV show"
              },
              "overview": {
                "type": "string",
                "description": "Overview or description of the show"
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
                "description": "Poster image path, may be null"
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote score"
              },
              "vote_count": {
                "type": "integer",
                "description": "Total number of votes"
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
          },
          "description": "List of TV shows airing today"
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages available"
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

    url = "https://api.themoviedb.org/3/tv/airing_today"
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
