import os
import requests


def Get_tv_season_images(series_id, season_number):
    """
    :API_description: Get the images that belong to a TV season.
    :param series_id: The ID of the TV series.
    :param season_number: The season number.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "TMDB ID of the season"
        },
        "posters": {
          "type": "array",
          "description": "Array of poster images for the season",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number",
                "description": "Aspect ratio of the image"
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
                "description": "ISO 639-1 language code, or null if unknown"
              },
              "file_path": {
                "type": "string",
                "description": "Relative path to the image file"
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
        "posters"
      ]
    }
    ```
    """
    url = f"https://api.themoviedb.org/3/tv/{series_id}/season/{season_number}/images"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
