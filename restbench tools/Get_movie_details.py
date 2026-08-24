import os
import requests


def Get_movie_details(movie_id):
    """
    :API_description: Get the top level details of a movie by ID.
    :param movie_id: The ID of the movie.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "adult": {
          "type": "boolean",
          "description": "Indicates if the movie is for adults."
        },
        "backdrop_path": {
          "type": [
            "string",
            "null"
          ],
          "description": "Path to the backdrop image."
        },
        "belongs_to_collection": {
          "type": [
            "object",
            "null"
          ],
          "description": "Collection that the movie belongs to.",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "poster_path": {
              "type": [
                "string",
                "null"
              ]
            },
            "backdrop_path": {
              "type": [
                "string",
                "null"
              ]
            }
          },
          "required": [
            "id",
            "name",
            "poster_path",
            "backdrop_path"
          ]
        },
        "budget": {
          "type": "integer",
          "description": "Movie budget in dollars."
        },
        "genres": {
          "type": "array",
          "description": "List of genres.",
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
          "type": [
            "string",
            "null"
          ],
          "description": "Official homepage URL."
        },
        "id": {
          "type": "integer",
          "description": "TMDB movie ID."
        },
        "imdb_id": {
          "type": [
            "string",
            "null"
          ],
          "description": "IMDB ID."
        },
        "origin_country": {
          "type": "array",
          "description": "Countries of origin.",
          "items": {
            "type": "string"
          }
        },
        "original_language": {
          "type": "string",
          "description": "Original language code."
        },
        "original_title": {
          "type": "string",
          "description": "Original title."
        },
        "overview": {
          "type": "string",
          "description": "Short description."
        },
        "popularity": {
          "type": "number",
          "description": "Popularity score."
        },
        "poster_path": {
          "type": [
            "string",
            "null"
          ],
          "description": "Path to the poster image."
        },
        "production_companies": {
          "type": "array",
          "description": "Production companies involved.",
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
          "description": "Countries where the movie was produced.",
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
        "release_date": {
          "type": "string",
          "description": "Release date (YYYY-MM-DD)."
        },
        "revenue": {
          "type": "integer",
          "description": "Revenue in dollars."
        },
        "runtime": {
          "type": "integer",
          "description": "Runtime in minutes."
        },
        "spoken_languages": {
          "type": "array",
          "description": "Spoken languages.",
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
          "description": "Release status."
        },
        "tagline": {
          "type": [
            "string",
            "null"
          ],
          "description": "Tagline."
        },
        "title": {
          "type": "string",
          "description": "Movie title."
        },
        "video": {
          "type": "boolean",
          "description": "Whether the movie has a video."
        },
        "vote_average": {
          "type": "number",
          "description": "Average vote score."
        },
        "vote_count": {
          "type": "integer",
          "description": "Number of votes."
        }
      },
      "required": [
        "adult",
        "backdrop_path",
        "belongs_to_collection",
        "budget",
        "genres",
        "homepage",
        "id",
        "imdb_id",
        "origin_country",
        "original_language",
        "original_title",
        "overview",
        "popularity",
        "poster_path",
        "production_companies",
        "production_countries",
        "release_date",
        "revenue",
        "runtime",
        "spoken_languages",
        "status",
        "tagline",
        "title",
        "video",
        "vote_average",
        "vote_count"
      ]
    }
    ```
    """
    if movie_id is None:
        raise ValueError("`movie_id` is required.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
