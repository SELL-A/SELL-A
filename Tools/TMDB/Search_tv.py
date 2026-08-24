import os
import requests


def Search_tv(query):
    """
    :API_description: Search for a TV show.
    :param query: Search for a TV show.
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
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Indicates if the TV show is for adults."
              },
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the backdrop image. Can be null if no image available."
              },
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "description": "Array of genre IDs associated with the TV show."
              },
              "id": {
                "type": "integer",
                "description": "Unique identifier for the TV show."
              },
              "origin_country": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "Array of country codes where the TV show originated."
              },
              "original_language": {
                "type": "string",
                "description": "Original language of the TV show (e.g., 'en')."
              },
              "original_name": {
                "type": "string",
                "description": "Original name of the TV show."
              },
              "overview": {
                "type": "string",
                "description": "Brief overview or plot summary."
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score of the TV show."
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the poster image. Can be null if no image available."
              },
              "first_air_date": {
                "type": "string",
                "description": "First air date in YYYY-MM-DD format."
              },
              "name": {
                "type": "string",
                "description": "Name of the TV show."
              },
              "vote_average": {
                "type": "number",
                "description": "Average user rating (0-10)."
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of user votes."
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
          },
          "description": "Array of TV show search results."
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages available."
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results available."
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

    url = "https://api.themoviedb.org/3/search/tv"
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
