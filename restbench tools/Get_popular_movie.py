import os
import requests


def Get_popular_movie():
    """
    :API_description: Get a list of movies ordered by popularity.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "The current page number"
        },
        "results": {
          "type": "array",
          "description": "A list of movies ordered by popularity",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Whether the movie is for adults"
              },
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
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
                "description": "Movie ID"
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
                "description": "Overview or plot summary"
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score"
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ],
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
                "description": "Whether the movie is a video"
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote score"
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
          }
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
        "page",
        "results",
        "total_pages",
        "total_results"
      ]
    }
    ```
    """

    url = "https://api.themoviedb.org/3/movie/popular"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
