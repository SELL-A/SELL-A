import os
import requests


def Get_review_details(review_id):
    """
    :API_description: Retrieve the details of a movie or TV show review.
    :param review_id: The ID of the review.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "The unique identifier for the review."
        },
        "author": {
          "type": "string",
          "description": "The display name of the author."
        },
        "author_details": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the author."
            },
            "username": {
              "type": "string",
              "description": "The username of the author."
            },
            "avatar_path": {
              "type": [
                "string",
                "null"
              ],
              "description": "The path to the author's avatar image. May be null."
            },
            "rating": {
              "type": [
                "number",
                "null"
              ],
              "description": "The rating given by the author (e.g., 1-10). May be null."
            }
          },
          "required": [
            "name",
            "username",
            "avatar_path",
            "rating"
          ],
          "description": "Detailed information about the review author."
        },
        "content": {
          "type": "string",
          "description": "The full text content of the review."
        },
        "created_at": {
          "type": "string",
          "description": "The date and time when the review was created, in ISO 8601 format."
        },
        "iso_639_1": {
          "type": "string",
          "description": "The ISO 639-1 language code for the review (e.g., 'en')."
        },
        "media_id": {
          "type": "integer",
          "description": "The ID of the media (movie or TV show) that the review is for."
        },
        "media_title": {
          "type": "string",
          "description": "The title of the media (movie or TV show)."
        },
        "media_type": {
          "type": "string",
          "description": "The type of media (e.g., 'movie' or 'tv')."
        },
        "updated_at": {
          "type": "string",
          "description": "The date and time when the review was last updated, in ISO 8601 format."
        },
        "url": {
          "type": "string",
          "description": "The URL to the review on TMDB."
        }
      },
      "required": [
        "id",
        "author",
        "author_details",
        "content",
        "created_at",
        "iso_639_1",
        "media_id",
        "media_title",
        "media_type",
        "updated_at",
        "url"
      ]
    }
    ```
    """
    if review_id is None:
        raise ValueError("`review_id` is required.")

    url = f"https://api.themoviedb.org/3/review/{review_id}"
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
