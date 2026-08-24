from ast import If
import os
import requests


def Get_tv_season_credits(series_id, season_number):
    """
    :API_description: Get the credits for TV season.
    :param series_id: The ID of the TV series.
    :param season_number: The season number.
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
                "description": "Whether the cast member is an adult performer"
              },
              "gender": {
                "type": "integer",
                "description": "Gender: 0=Unknown, 1=Female, 2=Male"
              },
              "id": {
                "type": "integer",
                "description": "Unique ID of the cast member"
              },
              "known_for_department": {
                "type": "string",
                "description": "Department the person is known for"
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
                "description": "Path to profile image"
              },
              "character": {
                "type": "string",
                "description": "Character played"
              },
              "credit_id": {
                "type": "string",
                "description": "Unique credit ID"
              },
              "order": {
                "type": "integer",
                "description": "Order of appearance in credits"
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
                "description": "Whether the crew member is an adult"
              },
              "gender": {
                "type": "integer",
                "description": "Gender: 0=Unknown, 1=Female, 2=Male"
              },
              "id": {
                "type": "integer",
                "description": "Unique ID of the crew member"
              },
              "known_for_department": {
                "type": "string",
                "description": "Department the person is known for"
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
                "description": "Path to profile image"
              },
              "credit_id": {
                "type": "string",
                "description": "Unique credit ID"
              },
              "department": {
                "type": "string",
                "description": "Department of the crew member"
              },
              "job": {
                "type": "string",
                "description": "Specific job title"
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
          "description": "Season ID"
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
    url = f"https://api.themoviedb.org/3/tv/{series_id}/season/{season_number}/credits"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
