import os
import requests


def Get_collection_details(collection_id):
    """
    :API_description: Get collection details by id.
    :param collection_id: The ID of the collection.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Collection ID"
        },
        "name": {
          "type": "string",
          "description": "Collection name"
        },
        "original_language": {
          "type": "string",
          "description": "Original language code"
        },
        "original_name": {
          "type": "string",
          "description": "Original name"
        },
        "overview": {
          "type": [
            "string",
            "null"
          ],
          "description": "Overview description"
        },
        "poster_path": {
          "type": [
            "string",
            "null"
          ],
          "description": "Poster image path"
        },
        "backdrop_path": {
          "type": [
            "string",
            "null"
          ],
          "description": "Backdrop image path"
        },
        "parts": {
          "type": "array",
          "description": "List of movies in the collection",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Adult content flag"
              },
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Backdrop image path"
              },
              "id": {
                "type": "integer",
                "description": "Movie ID"
              },
              "name": {
                "type": "string",
                "description": "Movie name"
              },
              "original_name": {
                "type": "string",
                "description": "Original movie name"
              },
              "overview": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Movie overview"
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Poster image path"
              },
              "media_type": {
                "type": "string",
                "description": "Media type (e.g., movie)"
              },
              "original_language": {
                "type": "string",
                "description": "Original language code"
              },
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "description": "Genre IDs"
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score"
              },
              "release_date": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Release date (YYYY-MM-DD)"
              },
              "video": {
                "type": "boolean",
                "description": "Video flag"
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote"
              },
              "vote_count": {
                "type": "integer",
                "description": "Vote count"
              }
            },
            "required": [
              "adult",
              "backdrop_path",
              "id",
              "name",
              "original_name",
              "overview",
              "poster_path",
              "media_type",
              "original_language",
              "genre_ids",
              "popularity",
              "release_date",
              "video",
              "vote_average",
              "vote_count"
            ]
          }
        }
      },
      "required": [
        "id",
        "name",
        "original_language",
        "original_name",
        "overview",
        "poster_path",
        "backdrop_path",
        "parts"
      ]
    }
    ```
    """
    if collection_id is None:
        raise ValueError("`collection_id` is required.")

    url = f"https://api.themoviedb.org/3/collection/{collection_id}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
