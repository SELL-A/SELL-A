import os
import requests


def Get_tv_episode_images(series_id, season_number, episode_number):
    """
    :API_description: Get the images that belong to a TV episode.
    :param series_id: The ID of the TV series.
    :param season_number: The season number.
    :param episode_number: The episode number.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The TMDB ID of the episode"
        },
        "stills": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number",
                "description": "The aspect ratio of the still image"
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
                "description": "ISO 639-1 language code (often null for stills)"
              },
              "file_path": {
                "type": "string",
                "description": "The relative path to the image file"
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
      },
      "required": [
        "id",
        "stills"
      ]
    }
    ```
    """
    if series_id is None:
        raise ValueError("`series_id` is required.")
    if season_number is None:
        raise ValueError("`season_number` is required.")
    if episode_number is None:
        raise ValueError("`episode_number` is required.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/images"
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
