import os
import requests


def Get_tv_series_reviews(series_id):
    """
    :API_description: Get the reviews that have been added to a TV show.
    :param series_id: The ID of the TV series.
    :response_schema:
    ```json
    {
      "type": "object",
      "required": [
        "id",
        "page",
        "results",
        "total_pages",
        "total_results"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "description": "The TMDB ID of the TV series."
        },
        "page": {
          "type": "integer",
          "description": "Current page number."
        },
        "results": {
          "type": "array",
          "description": "List of reviews.",
          "items": {
            "type": "object",
            "required": [
              "author",
              "author_details",
              "content",
              "created_at",
              "id",
              "updated_at",
              "url"
            ],
            "properties": {
              "author": {
                "type": "string",
                "description": "Author of the review."
              },
              "author_details": {
                "type": "object",
                "required": [
                  "name",
                  "username",
                  "avatar_path",
                  "rating"
                ],
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Display name of the author (may be empty)."
                  },
                  "username": {
                    "type": "string",
                    "description": "Username of the author."
                  },
                  "avatar_path": {
                    "type": [
                      "string",
                      "null"
                    ],
                    "description": "Path to the author's avatar image."
                  },
                  "rating": {
                    "type": "integer",
                    "description": "Rating given by the author (0-10 scale)."
                  }
                }
              },
              "content": {
                "type": "string",
                "description": "The review text."
              },
              "created_at": {
                "type": "string",
                "description": "ISO 8601 date when the review was created."
              },
              "id": {
                "type": "string",
                "description": "The review ID."
              },
              "updated_at": {
                "type": "string",
                "description": "ISO 8601 date when the review was last updated."
              },
              "url": {
                "type": "string",
                "description": "URL to the review on TMDB."
              }
            }
          }
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages."
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results."
        }
      }
    }
    ```
    """
    if series_id is None:
        raise ValueError("`series_id` is required.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}/reviews"
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
