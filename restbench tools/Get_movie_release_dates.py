import os
import requests


def Get_movie_release_dates(movie_id):
    """
    :API_description: Get the release dates and certifications for a movie.
    :param movie_id: The ID of the movie.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "The movie ID"
        },
        "results": {
          "type": "array",
          "description": "List of release date entries by country",
          "items": {
            "type": "object",
            "properties": {
              "iso_3166_1": {
                "type": "string",
                "description": "ISO 3166-1 country code"
              },
              "release_dates": {
                "type": "array",
                "description": "List of release dates for this country",
                "items": {
                  "type": "object",
                  "properties": {
                    "certification": {
                      "type": "string",
                      "description": "Age certification (may be empty)"
                    },
                    "descriptors": {
                      "type": "array",
                      "description": "List of descriptors (e.g., content warnings)",
                      "items": {
                        "type": "string"
                      }
                    },
                    "iso_639_1": {
                      "type": "string",
                      "description": "Language code (may be empty)"
                    },
                    "note": {
                      "type": "string",
                      "description": "Additional note about the release (optional)"
                    },
                    "release_date": {
                      "type": "string",
                      "description": "Release date in ISO 8601 format"
                    },
                    "type": {
                      "type": "integer",
                      "description": "Release type (1 = Premiere, 3 = Theatrical, 4 = Digital, 5 = Physical, 6 = TV, etc.)"
                    }
                  },
                  "required": [
                    "certification",
                    "descriptors",
                    "iso_639_1",
                    "release_date",
                    "type"
                  ]
                }
              }
            },
            "required": [
              "iso_3166_1",
              "release_dates"
            ]
          }
        }
      },
      "required": [
        "id",
        "results"
      ]
    }
    ```
    """
    if movie_id is None:
        raise ValueError("`movie_id` is required.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/release_dates"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
