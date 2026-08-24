import os
import requests


def Get_credit_details(credit_id):
    """
    :API_description: Get a movie or TV credit details by id.
    :param credit_id: The ID of the credit.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "credit_type": {
          "type": "string",
          "description": "The type of credit (e.g., cast or crew)"
        },
        "department": {
          "type": "string",
          "description": "Department of the credit"
        },
        "job": {
          "type": "string",
          "description": "Job title"
        },
        "media": {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": [
                "string",
                "null"
              ],
              "description": "Backdrop image path"
            },
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string",
              "description": "Title of the media (for TV shows name, for movies title)"
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
            "poster_path": {
              "type": [
                "string",
                "null"
              ],
              "description": "Poster image path"
            },
            "media_type": {
              "type": "string",
              "description": "Type of media (e.g., tv, movie)"
            },
            "genre_ids": {
              "type": "array",
              "items": {
                "type": "integer"
              },
              "description": "Array of genre IDs"
            },
            "popularity": {
              "type": "number"
            },
            "first_air_date": {
              "type": [
                "string",
                "null"
              ],
              "description": "First air date for TV shows (null for movies)"
            },
            "vote_average": {
              "type": "number"
            },
            "vote_count": {
              "type": "integer"
            },
            "origin_country": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Array of origin country codes"
            },
            "character": {
              "type": [
                "string",
                "null"
              ],
              "description": "Character name if credit type is cast"
            },
            "episodes": {
              "type": "array",
              "items": {
                "type": "object",
                "additionalProperties": true
              },
              "description": "Episodes (empty for movies)"
            },
            "seasons": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "air_date": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "episode_count": {
                    "type": "integer"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "name": {
                    "type": "string"
                  },
                  "overview": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "poster_path": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "season_number": {
                    "type": "integer"
                  },
                  "show_id": {
                    "type": "integer"
                  }
                },
                "required": [
                  "air_date",
                  "episode_count",
                  "id",
                  "name",
                  "overview",
                  "poster_path",
                  "season_number",
                  "show_id"
                ]
              },
              "description": "Seasons for TV shows"
            }
          },
          "required": [
            "adult",
            "backdrop_path",
            "id",
            "name",
            "original_language",
            "original_name",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "first_air_date",
            "vote_average",
            "vote_count",
            "origin_country",
            "character",
            "episodes",
            "seasons"
          ]
        },
        "media_type": {
          "type": "string",
          "description": "Media type (e.g., tv)"
        },
        "id": {
          "type": "string",
          "description": "Credit ID"
        },
        "person": {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "original_name": {
              "type": "string"
            },
            "media_type": {
              "type": "string",
              "description": "Always 'person'"
            },
            "popularity": {
              "type": "number"
            },
            "gender": {
              "type": "integer",
              "description": "Gender: 0=Unknown, 1=Female, 2=Male, 3=Non-binary"
            },
            "known_for_department": {
              "type": "string"
            },
            "profile_path": {
              "type": [
                "string",
                "null"
              ],
              "description": "Profile image path"
            }
          },
          "required": [
            "adult",
            "id",
            "name",
            "original_name",
            "media_type",
            "popularity",
            "gender",
            "known_for_department",
            "profile_path"
          ]
        }
      },
      "required": [
        "credit_type",
        "department",
        "job",
        "media",
        "media_type",
        "id",
        "person"
      ]
    }
    ```
    """
    if credit_id is None:
        raise ValueError("`credit_id` is required.")
    url = f"https://api.themoviedb.org/3/credit/{credit_id}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
