import os
import requests


def Get_movie_reviews(movie_id):
    """
    :API_description: Get the user reviews for a movie.
    :param movie_id: The ID of the movie.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The movie ID."
        },
        "page": {
          "type": "integer",
          "description": "Current page number."
        },
        "results": {
          "type": "array",
          "description": "List of user reviews.",
          "items": {
            "type": "object",
            "properties": {
              "author": {
                "type": "string",
                "description": "Author name."
              },
              "author_details": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Author's display name (may be empty)."
                  },
                  "username": {
                    "type": "string",
                    "description": "Author's username."
                  },
                  "avatar_path": {
                    "type": [
                      "string",
                      "null"
                    ],
                    "description": "Path to avatar image (may be null)."
                  },
                  "rating": {
                    "type": [
                      "integer",
                      "null"
                    ],
                    "description": "Rating given by the author (integer, may be null)."
                  }
                },
                "required": [
                  "name",
                  "username",
                  "avatar_path",
                  "rating"
                ]
              },
              "content": {
                "type": "string",
                "description": "The review text content."
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "description": "Timestamp when the review was created."
              },
              "id": {
                "type": "string",
                "description": "Review ID."
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "description": "Timestamp when the review was last updated."
              },
              "url": {
                "type": "string",
                "format": "uri",
                "description": "URL to the review on TMDB."
              }
            },
            "required": [
              "author",
              "author_details",
              "content",
              "created_at",
              "id",
              "updated_at",
              "url"
            ]
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
      },
      "required": [
        "id",
        "page",
        "results",
        "total_pages",
        "total_results"
      ]
    }
    ```
    """
    if movie_id is None:
        raise ValueError("`movie_id` is required.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
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
