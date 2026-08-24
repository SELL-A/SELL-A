import os
import requests


def Discover_tv(with_original_language=None, sort_by=None):
    """
    :API_description: Discover TV shows by different types of data like average rating, number of votes, genres, the network they aired on and air dates.
    :param with_original_language: Filter by original language, ISO 639-1 value (e.g. en).
    :param sort_by: Sort the results, e.g. vote_average.desc,name.desc,popularity.desc,vote average.desc.
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
          "description": "Array of TV show results.",
          "items": {
            "type": "object",
            "properties": {
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Backdrop image path (null if not available)."
              },
              "first_air_date": {
                "type": "string",
                "description": "First air date in YYYY-MM-DD format."
              },
              "genre_ids": {
                "type": "array",
                "description": "Array of genre IDs.",
                "items": {
                  "type": "integer"
                }
              },
              "id": {
                "type": "integer",
                "description": "Unique ID of the TV show."
              },
              "name": {
                "type": "string",
                "description": "Title of the TV show."
              },
              "origin_country": {
                "type": "array",
                "description": "Array of ISO 3166-1 country codes.",
                "items": {
                  "type": "string"
                }
              },
              "original_language": {
                "type": "string",
                "description": "Original language ISO 639-1 code."
              },
              "original_name": {
                "type": "string",
                "description": "Original name of the TV show."
              },
              "overview": {
                "type": "string",
                "description": "Overview or description of the TV show."
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
                "description": "Poster image path (null if not available)."
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
          "description": "Total number of pages available."
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results."
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

    url = "https://api.themoviedb.org/3/discover/tv"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    if not bearer_token:
        raise Exception("TMDB_BEARER_TOKEN is not set.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = {}
    if with_original_language is not None:
        params["with_original_language"] = with_original_language
    if sort_by is not None:
        params["sort_by"] = sort_by

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
