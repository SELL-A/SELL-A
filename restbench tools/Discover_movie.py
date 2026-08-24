import os
import requests


def Discover_movie(with_original_language=None, vote_average_gte=None, primary_release_date_gte=None, sort_by=None):
    """
    :API_description: Discover movies by different types of data like average rating, number of votes, genres and certifications.
    :param with_original_language: Filter by original language, ISO 639-1 value (e.g. en).
    :param vote_average_gte: Filter and only include movies with a rating greater than or equal to this value.
    :param primary_release_date_gte: Filter movies with a primary release date on or after this date. Format: YYYY-MM-DD.
    :param sort_by: Sort the results, e.g. vote_average.desc,name.desc,popularity.desc,vote average.desc.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
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
                "description": "Indicates if the movie is for adults"
              },
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to backdrop image, can be null"
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
                "description": "Unique movie ID"
              },
              "original_language": {
                "type": "string",
                "description": "ISO 639-1 language code"
              },
              "original_title": {
                "type": "string",
                "description": "Original title of the movie"
              },
              "overview": {
                "type": "string",
                "description": "Brief plot overview"
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
                "description": "Path to poster image, can be null"
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
                "description": "Indicates if the movie has a video"
              },
              "vote_average": {
                "type": "number",
                "description": "Average vote rating (0-10)"
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
          "description": "Total number of pages available"
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

    url = "https://api.themoviedb.org/3/discover/movie"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    if not bearer_token:
        raise Exception("TMDB_BEARER_TOKEN is not set.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = {"with_original_language": with_original_language, "vote_average.gte": vote_average_gte, "primary_release_date.gte": primary_release_date_gte, "sort_by": sort_by}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
