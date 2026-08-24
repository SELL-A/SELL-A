import os
import requests


def Get_popular_person():
    """
    :API_description: Get a list of people ordered by popularity.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "Current page number."
        },
        "results": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Whether the person is for adult audiences."
              },
              "gender": {
                "type": "integer",
                "description": "Gender: 0=Not specified, 1=Female, 2=Male."
              },
              "id": {
                "type": "integer",
                "description": "Unique ID of the person."
              },
              "known_for": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "adult": {
                      "type": "boolean",
                      "description": "Whether the media is adult content. May be absent for TV shows."
                    },
                    "backdrop_path": {
                      "type": [
                        "string",
                        "null"
                      ],
                      "description": "Path to backdrop image."
                    },
                    "genre_ids": {
                      "type": "array",
                      "items": {
                        "type": "integer"
                      },
                      "description": "Array of genre IDs."
                    },
                    "id": {
                      "type": "integer",
                      "description": "Unique ID of the media."
                    },
                    "media_type": {
                      "type": "string",
                      "description": "Type of media: 'movie' or 'tv'."
                    },
                    "original_language": {
                      "type": "string",
                      "description": "Original language code."
                    },
                    "overview": {
                      "type": "string",
                      "description": "Brief overview of the media."
                    },
                    "poster_path": {
                      "type": [
                        "string",
                        "null"
                      ],
                      "description": "Path to poster image."
                    },
                    "vote_average": {
                      "type": "number",
                      "description": "Average vote rating."
                    },
                    "vote_count": {
                      "type": "integer",
                      "description": "Number of votes."
                    },
                    "original_title": {
                      "type": "string",
                      "description": "Original title for movies. May be absent for TV."
                    },
                    "release_date": {
                      "type": [
                        "string",
                        "null"
                      ],
                      "description": "Release date for movies. May be absent for TV."
                    },
                    "title": {
                      "type": "string",
                      "description": "Title for movies. May be absent for TV."
                    },
                    "video": {
                      "type": "boolean",
                      "description": "Whether the movie has video. May be absent for TV."
                    },
                    "first_air_date": {
                      "type": [
                        "string",
                        "null"
                      ],
                      "description": "First air date for TV shows. May be absent for movies."
                    },
                    "name": {
                      "type": "string",
                      "description": "Name for TV shows. May be absent for movies."
                    },
                    "origin_country": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "description": "Origin country codes for TV shows. May be absent for movies."
                    },
                    "original_name": {
                      "type": "string",
                      "description": "Original name for TV shows. May be absent for movies."
                    }
                  },
                  "required": [
                    "id",
                    "media_type",
                    "original_language",
                    "overview",
                    "vote_average",
                    "vote_count"
                  ],
                  "description": "A media item that the person is known for (movie or TV show)."
                }
              },
              "known_for_department": {
                "type": "string",
                "description": "Department the person is known for, e.g., 'Acting'."
              },
              "name": {
                "type": "string",
                "description": "Name of the person."
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
              "adult",
              "gender",
              "id",
              "known_for",
              "known_for_department",
              "name",
              "popularity",
              "profile_path"
            ],
            "description": "A person object."
          }
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages."
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results."
        }
      },
      "required": [
        "page",
        "results",
        "total_pages",
        "total_results"
      ],
      "description": "Response from the Get Popular Person endpoint."
    }
    ```
    """

    url = "https://api.themoviedb.org/3/person/popular"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
