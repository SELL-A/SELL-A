import os
import requests


def Get_movie_genres():
    """
    :API_description: Get the list of official genres for movies.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "genres": {
          "type": "array",
          "description": "List of movie genres.",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "Genre ID."
              },
              "name": {
                "type": "string",
                "description": "Genre name."
              }
            },
            "required": [
              "id",
              "name"
            ]
          }
        }
      },
      "required": [
        "genres"
      ]
    }
    ```
    """

    url = "https://api.themoviedb.org/3/genre/movie/list"
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
