import os
import requests


def Get_latest_movie():
    """
    :API_description: Get the newest movie ID.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "adult": {
          "type": "boolean"
        },
        "backdrop_path": {
          "type": [
            "string",
            "null"
          ]
        },
        "belongs_to_collection": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true
        },
        "budget": {
          "type": "integer"
        },
        "genres": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          }
        },
        "homepage": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "imdb_id": {
          "type": [
            "string",
            "null"
          ]
        },
        "original_language": {
          "type": "string"
        },
        "original_title": {
          "type": "string"
        },
        "overview": {
          "type": "string"
        },
        "popularity": {
          "type": "number"
        },
        "poster_path": {
          "type": [
            "string",
            "null"
          ]
        },
        "production_companies": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          }
        },
        "production_countries": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          }
        },
        "release_date": {
          "type": "string"
        },
        "revenue": {
          "type": "integer"
        },
        "runtime": {
          "type": "integer"
        },
        "spoken_languages": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          }
        },
        "status": {
          "type": "string"
        },
        "tagline": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "video": {
          "type": "boolean"
        },
        "vote_average": {
          "type": "number"
        },
        "vote_count": {
          "type": "integer"
        }
      },
      "required": [
        "adult",
        "backdrop_path",
        "belongs_to_collection",
        "budget",
        "genres",
        "homepage",
        "id",
        "imdb_id",
        "original_language",
        "original_title",
        "overview",
        "popularity",
        "poster_path",
        "production_companies",
        "production_countries",
        "release_date",
        "revenue",
        "runtime",
        "spoken_languages",
        "status",
        "tagline",
        "title",
        "video",
        "vote_average",
        "vote_count"
      ]
    }
    ```
    """

    url = "https://api.themoviedb.org/3/movie/latest"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
