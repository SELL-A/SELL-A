import os
import requests


def Get_movie_credits(movie_id):
    """
    :API_description: Get the cast and crew for a movie.
    :param movie_id: The ID of the movie.
    :response_schema:
    ```json
    {
      "type": "object",
      "required": [
        "id",
        "cast",
        "crew"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "description": "The movie ID."
        },
        "cast": {
          "type": "array",
          "description": "List of cast members.",
          "items": {
            "type": "object",
            "required": [
              "adult",
              "gender",
              "id",
              "known_for_department",
              "name",
              "original_name",
              "popularity",
              "profile_path",
              "cast_id",
              "character",
              "credit_id",
              "order"
            ],
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Indicates if the cast member is for adult content."
              },
              "gender": {
                "type": "integer",
                "description": "Gender: 0 = unspecified, 1 = female, 2 = male."
              },
              "id": {
                "type": "integer",
                "description": "TMDB person ID."
              },
              "known_for_department": {
                "type": "string",
                "description": "The department the person is known for."
              },
              "name": {
                "type": "string",
                "description": "The person's name."
              },
              "original_name": {
                "type": "string",
                "description": "Original name (may differ from name)."
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score."
              },
              "profile_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Profile image path (can be null)."
              },
              "cast_id": {
                "type": "integer",
                "description": "Cast ID."
              },
              "character": {
                "type": "string",
                "description": "Character name played."
              },
              "credit_id": {
                "type": "string",
                "description": "Unique credit ID."
              },
              "order": {
                "type": "integer",
                "description": "Order in cast list."
              }
            }
          }
        },
        "crew": {
          "type": "array",
          "description": "List of crew members.",
          "items": {
            "type": "object",
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
            ],
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Indicates if the crew member is for adult content."
              },
              "gender": {
                "type": "integer",
                "description": "Gender: 0 = unspecified, 1 = female, 2 = male."
              },
              "id": {
                "type": "integer",
                "description": "TMDB person ID."
              },
              "known_for_department": {
                "type": "string",
                "description": "The department the person is known for."
              },
              "name": {
                "type": "string",
                "description": "The person's name."
              },
              "original_name": {
                "type": "string",
                "description": "Original name (may differ from name)."
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score."
              },
              "profile_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Profile image path (can be null)."
              },
              "credit_id": {
                "type": "string",
                "description": "Unique credit ID."
              },
              "department": {
                "type": "string",
                "description": "Crew department role."
              },
              "job": {
                "type": "string",
                "description": "Specific job within the department."
              }
            }
          }
        }
      }
    }
    ```
    """
    if movie_id is None:
        raise ValueError("`movie_id` is required.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
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
