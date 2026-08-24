import os
import requests


def Get_tv_episode_details(series_id, season_number, episode_number):
    """
    :API_description: Get the TV episode details by id.
    :param series_id: The ID of the TV series.
    :param season_number: The season number.
    :param episode_number: The episode number.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "air_date": {
          "type": "string",
          "description": "The air date of the episode."
        },
        "crew": {
          "type": "array",
          "description": "The crew for this episode.",
          "items": {
            "type": "object",
            "properties": {
              "department": {
                "type": "string"
              },
              "job": {
                "type": "string"
              },
              "credit_id": {
                "type": "string"
              },
              "adult": {
                "type": "boolean"
              },
              "gender": {
                "type": "integer"
              },
              "id": {
                "type": "integer"
              },
              "known_for_department": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "original_name": {
                "type": "string"
              },
              "popularity": {
                "type": "number"
              },
              "profile_path": {
                "type": [
                  "string",
                  "null"
                ]
              }
            },
            "required": [
              "department",
              "job",
              "credit_id",
              "adult",
              "gender",
              "id",
              "known_for_department",
              "name",
              "original_name",
              "popularity",
              "profile_path"
            ]
          }
        },
        "episode_number": {
          "type": "integer"
        },
        "guest_stars": {
          "type": "array",
          "description": "Guest stars in this episode.",
          "items": {
            "type": "object",
            "properties": {
              "character": {
                "type": "string"
              },
              "credit_id": {
                "type": "string"
              },
              "order": {
                "type": "integer"
              },
              "adult": {
                "type": "boolean"
              },
              "gender": {
                "type": "integer"
              },
              "id": {
                "type": "integer"
              },
              "known_for_department": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "original_name": {
                "type": "string"
              },
              "popularity": {
                "type": "number"
              },
              "profile_path": {
                "type": [
                  "string",
                  "null"
                ]
              }
            },
            "required": [
              "character",
              "credit_id",
              "order",
              "adult",
              "gender",
              "id",
              "known_for_department",
              "name",
              "original_name",
              "popularity",
              "profile_path"
            ]
          }
        },
        "name": {
          "type": "string"
        },
        "overview": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "production_code": {
          "type": "string"
        },
        "runtime": {
          "type": "integer"
        },
        "season_number": {
          "type": "integer"
        },
        "still_path": {
          "type": [
            "string",
            "null"
          ]
        },
        "vote_average": {
          "type": "number"
        },
        "vote_count": {
          "type": "integer"
        }
      },
      "required": [
        "air_date",
        "crew",
        "episode_number",
        "guest_stars",
        "name",
        "overview",
        "id",
        "production_code",
        "runtime",
        "season_number",
        "still_path",
        "vote_average",
        "vote_count"
      ]
    }
    ```
    """
    if series_id is None:
        raise ValueError("`series_id` is required.")
    if season_number is None:
        raise ValueError("`season_number` is required.")
    if episode_number is None:
        raise ValueError("`episode_number` is required.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}/season/{season_number}/episode/{episode_number}"
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
