import os
import requests


def Get_tv_latest_season_credits(series_id):
    """
    :API_description: Get the latest season credits of a TV show.
    :param series_id: The ID of the TV series.
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
                "description": "Indicates if the cast member is for adult content"
              },
              "gender": {
                "type": "integer",
                "description": "Gender: 0 unknown, 1 female, 2 male"
              },
              "id": {
                "type": "integer",
                "description": "TMDB person ID"
              },
              "known_for_department": {
                "type": "string",
                "description": "Known department, e.g., Acting"
              },
              "name": {
                "type": "string",
                "description": "Name of the cast member"
              },
              "original_name": {
                "type": "string",
                "description": "Original name of the cast member"
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
                "description": "Relative path to the profile image"
              },
              "character": {
                "type": "string",
                "description": "Character name played"
              },
              "credit_id": {
                "type": "string",
                "description": "Credit identifier"
              },
              "order": {
                "type": "integer",
                "description": "Order in the cast listing"
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
          }
        },
        "crew": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Indicates if the crew member is for adult content"
              },
              "gender": {
                "type": "integer",
                "description": "Gender: 0 unknown, 1 female, 2 male"
              },
              "id": {
                "type": "integer",
                "description": "TMDB person ID"
              },
              "known_for_department": {
                "type": "string",
                "description": "Known department, e.g., Production"
              },
              "name": {
                "type": "string",
                "description": "Name of the crew member"
              },
              "original_name": {
                "type": "string",
                "description": "Original name of the crew member"
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
                "description": "Relative path to the profile image"
              },
              "credit_id": {
                "type": "string",
                "description": "Credit identifier"
              },
              "department": {
                "type": "string",
                "description": "Department the crew member worked in"
              },
              "job": {
                "type": "string",
                "description": "Job title of the crew member"
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
              "credit_id",
              "department",
              "job"
            ]
          }
        },
        "id": {
          "type": "integer",
          "description": "TMDB series ID"
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
    if series_id is None:
        raise ValueError("`series_id` is required.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}/credits"
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
