import os
import requests


def Get_tv_details(series_id):
    """
    :API_description: Get the details of a TV show.
    :param series_id: The ID of the TV series.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "adult": {
          "type": "boolean",
          "description": "Indicates if the show is for adults."
        },
        "backdrop_path": {
          "type": "string",
          "description": "Backdrop image path."
        },
        "created_by": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "credit_id": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "gender": {
                "type": "integer"
              },
              "profile_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Profile image path or null."
              }
            },
            "required": [
              "id",
              "credit_id",
              "name",
              "gender",
              "profile_path"
            ]
          }
        },
        "episode_run_time": {
          "type": "array",
          "items": {
            "type": "integer"
          },
          "description": "Array of episode run times in minutes."
        },
        "first_air_date": {
          "type": "string",
          "description": "First air date in YYYY-MM-DD format."
        },
        "genres": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "name"
            ]
          }
        },
        "homepage": {
          "type": "string",
          "description": "Official website URL."
        },
        "id": {
          "type": "integer",
          "description": "TMDB series ID."
        },
        "in_production": {
          "type": "boolean"
        },
        "languages": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of spoken languages (ISO 639-1 codes)."
        },
        "last_air_date": {
          "type": "string",
          "description": "Last air date."
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
              "type": "integer"
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
          "type": "string",
          "description": "Series name."
        },
        "next_episode_to_air": {
          "anyOf": [
            {
              "type": "null"
            },
            {
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
                  "type": "integer"
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
              }
            }
          ]
        },
        "networks": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "logo_path": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "name": {
                "type": "string"
              },
              "origin_country": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "logo_path",
              "name",
              "origin_country"
            ]
          }
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
          },
          "description": "List of origin countries (ISO 3166-1 codes)."
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
          "type": "string",
          "description": "Poster image path."
        },
        "production_companies": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "logo_path": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "name": {
                "type": "string"
              },
              "origin_country": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "logo_path",
              "name",
              "origin_country"
            ]
          }
        },
        "production_countries": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "iso_3166_1": {
                "type": "string"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "iso_3166_1",
              "name"
            ]
          }
        },
        "seasons": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "air_date": {
                "type": "string"
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
              },
              "vote_average": {
                "type": "number"
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
              "vote_average"
            ]
          }
        },
        "spoken_languages": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "english_name": {
                "type": "string"
              },
              "iso_639_1": {
                "type": "string"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "english_name",
              "iso_639_1",
              "name"
            ]
          }
        },
        "status": {
          "type": "string",
          "description": "Series status (e.g., Ended, Returning Series)."
        },
        "tagline": {
          "type": "string"
        },
        "type": {
          "type": "string",
          "description": "Series type (e.g., Scripted)."
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
    if series_id is None:
        raise ValueError("`series_id` is required.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")