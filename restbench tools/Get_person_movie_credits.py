import os
import requests


def Get_person_movie_credits(person_id):
    """
    :API_description: Get the movie credits for a person, the results contains various information such as popularity and release date.
    :param person_id: The ID of the person.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "cast": {
          "type": "array",
          "items": {
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
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                }
              },
              "id": {
                "type": "integer"
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
              "release_date": {
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
              },
              "character": {
                "type": "string"
              },
              "credit_id": {
                "type": "string"
              },
              "order": {
                "type": "integer"
              }
            },
            "required": [
              "adult",
              "backdrop_path",
              "genre_ids",
              "id",
              "original_language",
              "original_title",
              "overview",
              "popularity",
              "poster_path",
              "release_date",
              "title",
              "video",
              "vote_average",
              "vote_count",
              "character",
              "credit_id",
              "order"
            ]
          }
        },
        "crew": {
          "type": "array",
          "items": {
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
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                }
              },
              "id": {
                "type": "integer"
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
              "release_date": {
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
              },
              "credit_id": {
                "type": "string"
              },
              "department": {
                "type": "string"
              },
              "job": {
                "type": "string"
              }
            },
            "required": [
              "adult",
              "backdrop_path",
              "genre_ids",
              "id",
              "original_language",
              "original_title",
              "overview",
              "popularity",
              "poster_path",
              "release_date",
              "title",
              "video",
              "vote_average",
              "vote_count",
              "credit_id",
              "department",
              "job"
            ]
          }
        },
        "id": {
          "type": "integer"
        }
      },
      "required": [
        "cast",
        "crew",
        "id"
      ]
    }
    ```
    """
    if person_id is None:
        raise ValueError("`person_id` is required.")

    url = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
