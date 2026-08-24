import os
import requests


def Get_movie_recommendations(movie_id):
    """
    :API_description: Get a list of recommended movies for a movie.
    :param movie_id: The ID of the movie.
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
          "description": "List of recommended movies.",
          "items": {
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
                "description": "Path to the backdrop image, may be null."
              },
              "id": {
                "type": "integer",
                "description": "TMDB movie ID."
              },
              "title": {
                "type": "string",
                "description": "Movie title."
              },
              "original_title": {
                "type": "string",
                "description": "Original movie title."
              },
              "overview": {
                "type": "string",
                "description": "Movie overview/synopsis."
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the poster image, may be null."
              },
              "media_type": {
                "type": "string",
                "description": "Media type, typically 'movie'."
              },
              "original_language": {
                "type": "string",
                "description": "Original language code (e.g., 'en')."
              },
              "genre_ids": {
                "type": "array",
                "description": "Array of genre IDs.",
                "items": {
                  "type": "integer"
                }
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score."
              },
              "release_date": {
                "type": "string",
                "description": "Release date (format YYYY-MM-DD)."
              },
              "softcore": {
                "type": "boolean",
                "description": "Indicates if movie is softcore."
              },
              "video": {
                "type": "boolean",
                "description": "Indicates if there is a video."
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
              "id",
              "title",
              "original_title",
              "overview",
              "poster_path",
              "media_type",
              "original_language",
              "genre_ids",
              "popularity",
              "release_date",
              "softcore",
              "video",
              "vote_average",
              "vote_count"
            ]
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
      ]
    }
    ```
    """
    if movie_id is None:
        raise ValueError("`movie_id` is required.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
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
