import os
import requests


def Get_now_playing_movies(region=None):
    """
    :API_description: Get a list of movies that are currently in theatres. This is a release type query that looks for all movies that have a release type of 2 or 3 within the specified date range.
    :param region: ISO-3166-1 code
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "dates": {
          "type": "object",
          "properties": {
            "maximum": {
              "type": "string",
              "description": "Maximum release date in YYYY-MM-DD format"
            },
            "minimum": {
              "type": "string",
              "description": "Minimum release date in YYYY-MM-DD format"
            }
          },
          "required": [
            "maximum",
            "minimum"
          ]
        },
        "page": {
          "type": "integer",
          "description": "Current page number"
        },
        "results": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Whether the movie is for adults"
              },
              "backdrop_path": {
                "type": "string",
                "description": "Path to the backdrop image"
              },
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "description": "Array of genre IDs"
              },
              "id": {
                "type": "integer",
                "description": "TMDB movie ID"
              },
              "original_language": {
                "type": "string",
                "description": "Original language code"
              },
              "original_title": {
                "type": "string",
                "description": "Original title"
              },
              "overview": {
                "type": "string",
                "description": "Movie overview/synopsis"
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score"
              },
              "poster_path": {
                "type": "string",
                "description": "Path to the poster image"
              },
              "release_date": {
                "type": "string",
                "description": "Release date in YYYY-MM-DD format"
              },
              "title": {
                "type": "string",
                "description": "Movie title"
              },
              "video": {
                "type": "boolean",
                "description": "Whether the movie has video"
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote score (0-10)"
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes"
              }
            },
            "required": [
              "adult",
              "backdrop_path",
              "genre_ids",
              "id",
              "original_language",
              "original_title",
              "overview",
              "popularity",
              "poster_path",
              "release_date",
              "title",
              "video",
              "vote_average",
              "vote_count"
            ]
          },
          "description": "List of movies currently in theatres"
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages"
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results"
        }
      },
      "required": [
        "dates",
        "page",
        "results",
        "total_pages",
        "total_results"
      ]
    }
    ```
    """

    url = "https://api.themoviedb.org/3/movie/now_playing"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    if not bearer_token:
        raise Exception("TMDB_BEARER_TOKEN is not set.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = {}
    if region is not None:
        params["region"] = region

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
