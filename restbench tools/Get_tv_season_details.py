import os
import requests


def Get_tv_season_details(series_id, season_number):
    """
    :API_description: Get the TV season details by id.
    :param series_id: The ID of the TV series.
    :param season_number: The season number.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "_id": {
          "type": "string",
          "description": "TMDB internal ID for the season."
        },
        "air_date": {
          "type": "string",
          "description": "The air date of the season (format: YYYY-MM-DD)."
        },
        "episodes": {
          "type": "array",
          "description": "List of episodes in the season.",
          "items": {
            "type": "object",
            "properties": {
              "air_date": {
                "type": "string",
                "description": "Air date of the episode."
              },
              "episode_number": {
                "type": "integer",
                "description": "Episode number within the season."
              },
              "episode_type": {
                "type": "string",
                "description": "Type of episode (e.g., standard, finale)."
              },
              "id": {
                "type": "integer",
                "description": "TMDB ID for the episode."
              },
              "name": {
                "type": "string",
                "description": "Name/title of the episode."
              },
              "overview": {
                "type": "string",
                "description": "Synopsis or plot summary of the episode."
              },
              "production_code": {
                "type": "string",
                "description": "Production code of the episode."
              },
              "runtime": {
                "type": "integer",
                "description": "Runtime of the episode in minutes."
              },
              "season_number": {
                "type": "integer",
                "description": "Season number this episode belongs to."
              },
              "show_id": {
                "type": "integer",
                "description": "TMDB ID of the TV series."
              },
              "still_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the episode still image."
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote rating for the episode."
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes for the episode."
              },
              "crew": {
                "type": "array",
                "description": "Crew members for the episode.",
                "items": {
                  "type": "object",
                  "properties": {
                    "department": {
                      "type": "string",
                      "description": "Department of the crew member (e.g., Directing, Writing)."
                    },
                    "job": {
                      "type": "string",
                      "description": "Specific job title (e.g., Director, Writer)."
                    },
                    "credit_id": {
                      "type": "string",
                      "description": "TMDB credit ID."
                    },
                    "adult": {
                      "type": "boolean",
                      "description": "Indicates if the person is an adult performer."
                    },
                    "gender": {
                      "type": "integer",
                      "description": "Gender: 0=Unknown, 1=Female, 2=Male."
                    },
                    "id": {
                      "type": "integer",
                      "description": "TMDB person ID."
                    },
                    "known_for_department": {
                      "type": "string",
                      "description": "Department the person is known for."
                    },
                    "name": {
                      "type": "string",
                      "description": "Name of the crew member."
                    },
                    "original_name": {
                      "type": "string",
                      "description": "Original name of the crew member."
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
                      "description": "Path to the person's profile image."
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
              "guest_stars": {
                "type": "array",
                "description": "Guest stars in the episode.",
                "items": {
                  "type": "object",
                  "properties": {
                    "character": {
                      "type": "string",
                      "description": "Character name played by the guest star."
                    },
                    "credit_id": {
                      "type": "string",
                      "description": "TMDB credit ID."
                    },
                    "order": {
                      "type": "integer",
                      "description": "Order of appearance."
                    },
                    "adult": {
                      "type": "boolean",
                      "description": "Indicates if the person is an adult performer."
                    },
                    "gender": {
                      "type": "integer",
                      "description": "Gender: 0=Unknown, 1=Female, 2=Male."
                    },
                    "id": {
                      "type": "integer",
                      "description": "TMDB person ID."
                    },
                    "known_for_department": {
                      "type": "string",
                      "description": "Department the person is known for."
                    },
                    "name": {
                      "type": "string",
                      "description": "Name of the guest star."
                    },
                    "original_name": {
                      "type": "string",
                      "description": "Original name of the guest star."
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
                      "description": "Path to the person's profile image."
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
              }
            },
            "required": [
              "air_date",
              "episode_number",
              "episode_type",
              "id",
              "name",
              "overview",
              "production_code",
              "runtime",
              "season_number",
              "show_id",
              "still_path",
              "vote_average",
              "vote_count",
              "crew",
              "guest_stars"
            ]
          }
        },
        "name": {
          "type": "string",
          "description": "Name of the season (e.g., Season 1)."
        },
        "networks": {
          "type": "array",
          "description": "List of networks that aired the season.",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "TMDB network ID."
              },
              "logo_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the network's logo image."
              },
              "name": {
                "type": "string",
                "description": "Name of the network."
              },
              "origin_country": {
                "type": "string",
                "description": "Country code of origin (e.g., US)."
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
        "overview": {
          "type": "string",
          "description": "General overview/synopsis of the season."
        },
        "id": {
          "type": "integer",
          "description": "TMDB season ID."
        },
        "poster_path": {
          "type": [
            "string",
            "null"
          ],
          "description": "Path to the season poster image."
        },
        "season_number": {
          "type": "integer",
          "description": "Season number."
        },
        "vote_average": {
          "type": "number",
          "description": "Average vote rating for the season."
        }
      },
      "required": [
        "_id",
        "air_date",
        "episodes",
        "name",
        "networks",
        "overview",
        "id",
        "poster_path",
        "season_number",
        "vote_average"
      ]
    }
    ```
    """
    url = f"https://api.themoviedb.org/3/tv/{series_id}/season/{season_number}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
