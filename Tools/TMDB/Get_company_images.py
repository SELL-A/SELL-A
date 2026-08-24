import os
import requests


def Get_company_images(company_id):
    """
    :API_description: Get a companies logos by id.
    :param company_id: The ID of the company.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The company ID."
        },
        "logos": {
          "type": "array",
          "description": "An array of logo images for the company.",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number",
                "description": "The aspect ratio of the image."
              },
              "file_path": {
                "type": "string",
                "description": "The file path for the image."
              },
              "height": {
                "type": "integer",
                "description": "The height of the image in pixels."
              },
              "id": {
                "type": "string",
                "description": "The unique identifier for the logo."
              },
              "file_type": {
                "type": "string",
                "description": "The file type extension (e.g., .svg)."
              },
              "vote_average": {
                "type": "number",
                "description": "The average vote score for the image."
              },
              "vote_count": {
                "type": "integer",
                "description": "The number of votes for the image."
              },
              "width": {
                "type": "integer",
                "description": "The width of the image in pixels."
              }
            },
            "required": [
              "aspect_ratio",
              "file_path",
              "height",
              "id",
              "file_type",
              "vote_average",
              "vote_count",
              "width"
            ]
          }
        }
      },
      "required": [
        "id",
        "logos"
      ]
    }
    ```
    """
    if company_id is None:
        raise ValueError("`company_id` is required.")

    url = f"https://api.themoviedb.org/3/company/{company_id}/images"
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
