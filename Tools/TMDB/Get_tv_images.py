import os
import requests


def Get_tv_images(series_id):
    """
    :API_description: Get the images that belong to a TV series.
    :param series_id: The ID of the TV series.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "backdrops": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number",
                "description": "Aspect ratio of the image"
              },
              "height": {
                "type": "integer",
                "description": "Height in pixels"
              },
              "iso_639_1": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "ISO 639-1 language code or null"
              },
              "file_path": {
                "type": "string",
                "description": "Relative path to the image"
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote rating"
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes"
              },
              "width": {
                "type": "integer",
                "description": "Width in pixels"
              }
            },
            "required": [
              "aspect_ratio",
              "height",
              "iso_639_1",
              "file_path",
              "vote_average",
              "vote_count",
              "width"
            ]
          }
        },
        "logos": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number"
              },
              "height": {
                "type": "integer"
              },
              "iso_639_1": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "file_path": {
                "type": "string"
              },
              "vote_average": {
                "type": "number"
              },
              "vote_count": {
                "type": "integer"
              },
              "width": {
                "type": "integer"
              }
            },
            "required": [
              "aspect_ratio",
              "height",
              "iso_639_1",
              "file_path",
              "vote_average",
              "vote_count",
              "width"
            ]
          }
        },
        "posters": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number"
              },
              "height": {
                "type": "integer"
              },
              "iso_639_1": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "file_path": {
                "type": "string"
              },
              "vote_average": {
                "type": "number"
              },
              "vote_count": {
                "type": "integer"
              },
              "width": {
                "type": "integer"
              }
            },
            "required": [
              "aspect_ratio",
              "height",
              "iso_639_1",
              "file_path",
              "vote_average",
              "vote_count",
              "width"
            ]
          }
        },
        "id": {
          "type": "integer",
          "description": "The TV series ID"
        }
      },
      "required": [
        "backdrops",
        "logos",
        "posters",
        "id"
      ]
    }
    ```
    """
    if series_id is None:
        raise ValueError("`series_id` is required.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}/images"
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
