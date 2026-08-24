import os
import requests


def Get_top_rated_tv():
    """
    :API_description: Get a list of the top rated TV shows on TMDb.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "The current page number."
        },
        "results": {
          "type": "array",
          "description": "A list of top rated TV shows.",
          "items": {
            "type": "object",
            "properties": {
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the backdrop image, can be null."
              },
              "first_air_date": {
                "type": "string",
                "description": "The first air date of the TV show."
              },
              "genre_ids": {
                "type": "array",
                "description": "An array of genre IDs.",
                "items": {
                  "type": "integer"
                }
              },
              "id": {
                "type": "integer",
                "description": "The unique identifier for the TV show."
              },
              "name": {
                "type": "string",
                "description": "The name of the TV show."
              },
              "origin_country": {
                "type": "array",
                "description": "An array of origin country codes.",
                "items": {
                  "type": "string"
                }
              },
              "original_language": {
                "type": "string",
                "description": "The original language of the TV show."
              },
              "original_name": {
                "type": "string",
                "description": "The original name of the TV show."
              },
              "overview": {
                "type": "string",
                "description": "A brief overview or synopsis of the TV show."
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score."
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the poster image, can be null."
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote score."
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes."
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
          "description": "The total number of pages."
        },
        "total_results": {
          "type": "integer",
          "description": "The total number of results."
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

    url = "https://api.themoviedb.org/3/tv/top_rated"
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
