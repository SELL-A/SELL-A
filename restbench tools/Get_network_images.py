import os
import requests


def Get_network_images(network_id):
    """
    :API_description: Get the TV network logos by id.
    :param network_id: The ID of the network.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The ID of the network"
        },
        "logos": {
          "type": "array",
          "description": "Array of logo images",
          "items": {
            "type": "object",
            "properties": {
              "aspect_ratio": {
                "type": "number"
              },
              "file_path": {
                "type": "string"
              },
              "height": {
                "type": "integer"
              },
              "id": {
                "type": "string"
              },
              "file_type": {
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
    if network_id is None:
        raise ValueError("`network_id` is required.")

    url = f"https://api.themoviedb.org/3/network/{network_id}/images"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
