import os
import requests


def Get_tv_episode_credits(series_id, season_number, episode_number):
    """
    :API_description: Get the credits (cast, crew and guest stars) for a TV episode.
    :param series_id: The ID of the TV series.
    :param season_number: The season number.
    :param episode_number: The episode number.
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
                "type": "boolean",
                "description": "Whether the person is adult content"
              },
              "gender": {
                "type": "integer",
                "description": "Gender: 0=Not specified, 1=Female, 2=Male, 3=Non-binary"
              },
              "id": {
                "type": "integer",
                "description": "Person ID"
              },
              "known_for_department": {
                "type": "string",
                "description": "Known department (e.g., Acting)"
              },
              "name": {
                "type": "string",
                "description": "Person's name"
              },
              "original_name": {
                "type": "string",
                "description": "Original name"
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score"
              },
              "profile_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to profile image or null"
              },
              "character": {
                "type": "string",
                "description": "Character played"
              },
              "credit_id": {
                "type": "string",
                "description": "Credit ID"
              },
              "order": {
                "type": "integer",
                "description": "Order in cast list"
              }
            },
            "required": [
              "adult",
              "gender",
              "id",
              "known_for_department",
              "name",
              "original_name",
              "popularity",
              "profile_path",
              "character",
              "credit_id",
              "order"
            ]
          },
          "description": "Array of cast members"
        },
        "crew": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "department": {
                "type": "string",
                "description": "Department (e.g., Directing)"
              },
              "job": {
                "type": "string",
                "description": "Job title (e.g., Director)"
              },
              "credit_id": {
                "type": "string",
                "description": "Credit ID"
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
          },
          "description": "Array of crew members"
        },
        "guest_stars": {
          "type": "array",
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
          },
          "description": "Array of guest stars"
        },
        "id": {
          "type": "integer",
          "description": "Episode ID"
        }
      },
      "required": [
        "cast",
        "crew",
        "guest_stars",
        "id"
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

    url = f"https://api.themoviedb.org/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/credits"
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
