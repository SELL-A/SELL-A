import os
import requests


def Get_latest_tv():
    """
    :API_description: Get the newest TV show ID.
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
        "created_by": {
          "type": "array",
          "items": {}
        },
        "episode_run_time": {
          "type": "array",
          "items": {}
        },
        "first_air_date": {
          "type": "string"
        },
        "genres": {
          "type": "array",
          "items": {}
        },
        "homepage": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "in_production": {
          "type": "boolean"
        },
        "languages": {
          "type": "array",
          "items": {}
        },
        "last_air_date": {
          "type": "string"
        },
        "last_episode_to_air": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "overview": {
              "type": "string"
            },
            "vote_average": {
              "type": "number"
            },
            "vote_count": {
              "type": "integer"
            },
            "air_date": {
              "type": "string"
            },
            "episode_number": {
              "type": "integer"
            },
            "production_code": {
              "type": "string"
            },
            "runtime": {
              "type": [
                "number",
                "null"
              ]
            },
            "season_number": {
              "type": "integer"
            },
            "show_id": {
              "type": "integer"
            },
            "still_path": {
              "type": [
                "string",
                "null"
              ]
            }
          },
          "required": [
            "id",
            "name",
            "overview",
            "vote_average",
            "vote_count",
            "air_date",
            "episode_number",
            "production_code",
            "runtime",
            "season_number",
            "show_id",
            "still_path"
          ]
        },
        "name": {
          "type": "string"
        },
        "next_episode_to_air": {
          "type": [
            "object",
            "null"
          ],
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "overview": {
              "type": "string"
            },
            "vote_average": {
              "type": "number"
            },
            "vote_count": {
              "type": "integer"
            },
            "air_date": {
              "type": "string"
            },
            "episode_number": {
              "type": "integer"
            },
            "production_code": {
              "type": "string"
            },
            "runtime": {
              "type": [
                "number",
                "null"
              ]
            },
            "season_number": {
              "type": "integer"
            },
            "show_id": {
              "type": "integer"
            },
            "still_path": {
              "type": [
                "string",
                "null"
              ]
            }
          },
          "required": [
            "id",
            "name",
            "overview",
            "vote_average",
            "vote_count",
            "air_date",
            "episode_number",
            "production_code",
            "runtime",
            "season_number",
            "show_id",
            "still_path"
          ]
        },
        "networks": {
          "type": "array",
          "items": {}
        },
        "number_of_episodes": {
          "type": "integer"
        },
        "number_of_seasons": {
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
        "production_companies": {
          "type": "array",
          "items": {}
        },
        "production_countries": {
          "type": "array",
          "items": {}
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
                "type": "string"
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "season_number": {
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
              "season_number"
            ]
          }
        },
        "spoken_languages": {
          "type": "array",
          "items": {}
        },
        "status": {
          "type": "string"
        },
        "tagline": {
          "type": "string"
        },
        "type": {
          "type": "string"
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
        "created_by",
        "episode_run_time",
        "first_air_date",
        "genres",
        "homepage",
        "id",
        "in_production",
        "languages",
        "last_air_date",
        "last_episode_to_air",
        "name",
        "next_episode_to_air",
        "networks",
        "number_of_episodes",
        "number_of_seasons",
        "origin_country",
        "original_language",
        "original_name",
        "overview",
        "popularity",
        "poster_path",
        "production_companies",
        "production_countries",
        "seasons",
        "spoken_languages",
        "status",
        "tagline",
        "type",
        "vote_average",
        "vote_count"
      ]
    }
    ```
    """

    url = "https://api.themoviedb.org/3/tv/latest"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
