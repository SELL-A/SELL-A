import os
import requests


def Get_person_tv_credits(person_id):
    """
    :API_description: Get the TV credits that belong to a person.
    :param person_id: The ID of the person.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "cast": {
          "type": "array",
          "description": "List of cast credits for TV shows",
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
              "origin_country": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "original_language": {
                "type": "string"
              },
              "original_name": {
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
              "first_air_date": {
                "type": "string"
              },
              "name": {
                "type": "string"
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
              "episode_count": {
                "type": "integer"
              }
            },
            "required": [
              "adult",
              "backdrop_path",
              "genre_ids",
              "id",
              "origin_country",
              "original_language",
              "original_name",
              "overview",
              "popularity",
              "poster_path",
              "first_air_date",
              "name",
              "vote_average",
              "vote_count",
              "character",
              "credit_id",
              "episode_count"
            ]
          }
        },
        "crew": {
          "type": "array",
          "description": "List of crew credits for TV shows",
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
              "origin_country": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "original_language": {
                "type": "string"
              },
              "original_name": {
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
              "first_air_date": {
                "type": "string"
              },
              "name": {
                "type": "string"
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
              "episode_count": {
                "type": "integer"
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
              "origin_country",
              "original_language",
              "original_name",
              "overview",
              "popularity",
              "poster_path",
              "first_air_date",
              "name",
              "vote_average",
              "vote_count",
              "credit_id",
              "department",
              "episode_count",
              "job"
            ]
          }
        },
        "id": {
          "type": "integer",
          "description": "The person's TMDB ID"
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

    url = f"https://api.themoviedb.org/3/person/{person_id}/tv_credits"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
