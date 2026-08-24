import os
import requests


def Get_movie_images(movie_id):
    """
    :API_description: Get the images that belong to a movie.
    :param movie_id: The ID of the movie.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "backdrops": {
          "type": "array",
          "description": "Array of backdrop images for the movie.",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number",
                "description": "Aspect ratio of the image."
              },
              "height": {
                "type": "integer",
                "description": "Height of the image in pixels."
              },
              "iso_639_1": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "ISO 639-1 language code, or null if not applicable."
              },
              "file_path": {
                "type": "string",
                "description": "Relative path to the image file."
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote score for the image."
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes for the image."
              },
              "width": {
                "type": "integer",
                "description": "Width of the image in pixels."
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
          "description": "The movie ID."
        },
        "logos": {
          "type": "array",
          "description": "Array of logo images for the movie.",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number",
                "description": "Aspect ratio of the logo."
              },
              "height": {
                "type": "integer",
                "description": "Height of the logo in pixels."
              },
              "iso_639_1": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "ISO 639-1 language code, or null if not applicable."
              },
              "file_path": {
                "type": "string",
                "description": "Relative path to the logo file."
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote score for the logo."
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes for the logo."
              },
              "width": {
                "type": "integer",
                "description": "Width of the logo in pixels."
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
          "description": "Array of poster images for the movie.",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number",
                "description": "Aspect ratio of the poster."
              },
              "height": {
                "type": "integer",
                "description": "Height of the poster in pixels."
              },
              "iso_639_1": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "ISO 639-1 language code, or null if not applicable."
              },
              "file_path": {
                "type": "string",
                "description": "Relative path to the poster file."
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote score for the poster."
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes for the poster."
              },
              "width": {
                "type": "integer",
                "description": "Width of the poster in pixels."
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
      },
      "required": [
        "backdrops",
        "id",
        "logos",
        "posters"
      ]
    }
    ```
    """
    if movie_id is None:
        raise ValueError("`movie_id` is required.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
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
