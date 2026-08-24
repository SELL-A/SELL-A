import os
import requests


def Get_tv_recommendations(series_id):
    """
    :API_description: Get the list of TV show recommendations for this item.
    :param series_id: The ID of the TV series.
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
          "description": "List of recommended TV shows",
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
                "description": "Backdrop image path"
              },
              "id": {
                "type": "integer",
                "description": "TMDB ID"
              },
              "name": {
                "type": "string",
                "description": "TV show name"
              },
              "original_language": {
                "type": "string"
              },
              "original_name": {
                "type": "string"
              },
              "overview": {
                "type": "string",
                "description": "Plot overview"
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Poster image path"
              },
              "media_type": {
                "type": "string",
                "description": "Media type, e.g., 'tv'"
              },
              "genre_ids": {
                "type": "array",
                "description": "Genre IDs",
                "items": {
                  "type": "integer"
                }
              },
              "popularity": {
                "type": "number"
              },
              "first_air_date": {
                "type": "string",
                "description": "First air date in YYYY-MM-DD"
              },
              "vote_average": {
                "type": "number"
              },
              "vote_count": {
                "type": "integer"
              },
              "origin_country": {
                "type": "array",
                "description": "Country codes",
                "items": {
                  "type": "string"
                }
              }
            },
            "required": [
              "adult",
              "backdrop_path",
              "id",
              "name",
              "original_language",
              "original_name",
              "overview",
              "poster_path",
              "media_type",
              "genre_ids",
              "popularity",
              "first_air_date",
              "vote_average",
              "vote_count",
              "origin_country"
            ]
          }
        },
        "total_pages": {
          "type": "integer",
          "description": "Total pages"
        },
        "total_results": {
          "type": "integer",
          "description": "Total results"
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

    url = f"https://api.themoviedb.org/3/tv/{series_id}/recommendations"
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
