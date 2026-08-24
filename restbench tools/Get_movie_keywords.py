import os
import requests


def Get_movie_keywords(movie_id):
    """
    :API_description: Get the keywords that have been added to a movie.
    :param movie_id: The ID of the movie.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The movie ID"
        },
        "keywords": {
          "type": "array",
          "description": "List of keywords associated with the movie",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "Keyword ID"
              },
              "name": {
                "type": "string",
                "description": "Keyword name"
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
        "id",
        "keywords"
      ]
    }
    ```
    """
    if movie_id is None:
        raise ValueError("`movie_id` is required.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/keywords"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
