import os
import requests


def Get_tv_keywords(series_id):
    """
    :API_description: Get a list of keywords that have been added to a TV show.
    :param series_id: The ID of the TV series.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The TMDB ID of the TV series."
        },
        "results": {
          "type": "array",
          "description": "List of keywords associated with the TV series.",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the keyword."
              },
              "id": {
                "type": "integer",
                "description": "The TMDB ID of the keyword."
              }
            },
            "required": [
              "name",
              "id"
            ]
          }
        }
      },
      "required": [
        "id",
        "results"
      ]
    }
    ```
    """
    if series_id is None:
        raise ValueError("`series_id` is required.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}/keywords"
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
