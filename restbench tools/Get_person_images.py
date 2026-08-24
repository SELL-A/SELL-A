import os
import requests


def Get_person_images(person_id):
    """
    :API_description: Get the profile images that belong to a person.
    :param person_id: The ID of the person.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The person ID."
        },
        "profiles": {
          "type": "array",
          "description": "Profile images for the person.",
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
                "description": "ISO 639-1 language code (may be null)."
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
        }
      },
      "required": [
        "id",
        "profiles"
      ]
    }
    ```
    """
    if person_id is None:
        raise ValueError("`person_id` is required.")
    url = f"https://api.themoviedb.org/3/person/{person_id}/images"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
