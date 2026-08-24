import os
import requests


def Get_network_details(network_id):
    """
    :API_description: Get the details of a network.
    :param network_id: The ID of the network.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "headquarters": {
          "type": "string",
          "description": "The headquarters location of the network"
        },
        "homepage": {
          "type": "string",
          "description": "The homepage URL of the network"
        },
        "id": {
          "type": "integer",
          "description": "The unique identifier of the network"
        },
        "logo_path": {
          "type": "string",
          "description": "The path to the logo image of the network"
        },
        "name": {
          "type": "string",
          "description": "The name of the network"
        },
        "origin_country": {
          "type": "string",
          "description": "The country code of the network's origin"
        }
      },
      "required": [
        "headquarters",
        "homepage",
        "id",
        "logo_path",
        "name",
        "origin_country"
      ]
    }
    ```
    """
    if network_id is None:
        raise ValueError("`network_id` is required.")

    url = f"https://api.themoviedb.org/3/network/{network_id}"
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
