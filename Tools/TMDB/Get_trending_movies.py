import os
import requests


def Get_trending_movies(time_window):
    """
    :API_description: Get the trending movies on TMDB.
    :param time_window: The time window for the trending results. Allowed values: day, week.
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
          "description": "List of trending movies.",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Indicates if the movie is for adults."
              },
              "backdrop_path": {
                "type": "string",
                "description": "Path to the backdrop image."
              },
              "id": {
                "type": "integer",
                "description": "TMDB movie ID."
              },
              "title": {
                "type": "string",
                "description": "Movie title."
              },
              "original_language": {
                "type": "string",
                "description": "Original language code."
              },
              "original_title": {
                "type": "string",
                "description": "Original movie title."
              },
              "overview": {
                "type": "string",
                "description": "Brief plot overview."
              },
              "poster_path": {
                "type": "string",
                "description": "Path to the poster image."
              },
              "media_type": {
                "type": "string",
                "description": "Media type, always 'movie' for this endpoint."
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
                "description": "Release date in YYYY-MM-DD format."
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
              "original_language",
              "original_title",
              "overview",
              "poster_path",
              "media_type",
              "genre_ids",
              "popularity",
              "release_date",
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
    if time_window is None:
        raise ValueError("`time_window` is required.")

    url = f"https://api.themoviedb.org/3/trending/movie/{time_window}"
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
