import os
import requests


def Get_tv_genre_list():
    """
    :API_description: Get the list of official genres for TV shows.
    :response_schema:
    ```json
    {
      "type": "object",
      "required": [
        "genres"
      ],
      "properties": {
        "genres": {
          "type": "array",
          "description": "A list of TV show genres.",
          "items": {
            "type": "object",
            "required": [
              "id",
              "name"
            ],
            "properties": {
              "id": {
                "type": "integer",
                "description": "The unique identifier for the genre."
              },
              "name": {
                "type": "string",
                "description": "The name of the genre."
              }
            }
          }
        }
      }
    }
    ```
    """

    url = "https://api.themoviedb.org/3/genre/tv/list"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
