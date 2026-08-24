import os
import requests


def Get_collection_images(collection_id):
    """
    :API_description: Get the images that belong to a collection.
    :param collection_id: The ID of the collection.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The collection ID"
        },
        "backdrops": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/image"
          }
        },
        "posters": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/image"
          }
        }
      },
      "required": [
        "id",
        "backdrops",
        "posters"
      ],
      "$defs": {
        "image": {
          "type": "object",
          "properties": {
            "aspect_ratio": {
              "type": "number",
              "description": "Aspect ratio of the image (width / height)"
            },
            "height": {
              "type": "integer",
              "description": "Height of the image in pixels"
            },
            "iso_639_1": {
              "type": [
                "string",
                "null"
              ],
              "description": "ISO 639-1 language code for the image, or null if language-neutral"
            },
            "file_path": {
              "type": "string",
              "description": "Relative path to the image file (e.g., /d8duYyyC9J5T825Hg7grmaabfxQ.jpg)"
            },
            "vote_average": {
              "type": "number",
              "description": "Average vote score for the image"
            },
            "vote_count": {
              "type": "integer",
              "description": "Number of votes for the image"
            },
            "width": {
              "type": "integer",
              "description": "Width of the image in pixels"
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
      }
    }
    ```
    """
    if collection_id is None:
        raise ValueError("`collection_id` is required.")

    url = f"https://api.themoviedb.org/3/collection/{collection_id}/images"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
