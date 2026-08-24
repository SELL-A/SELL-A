import os
import requests


def Get_trending_tv(time_window):
    """
    :API_description: Get the trending TV shows on TMDB.
    :param time_window: The time window for the trending results. Allowed values: day, week.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "The current page number."
        },
        "results": {
          "type": "array",
          "description": "A list of trending TV shows.",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Indicates if the TV show is for adults."
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
                "description": "The TMDB ID of the TV show."
              },
              "name": {
                "type": "string",
                "description": "The name of the TV show."
              },
              "original_language": {
                "type": "string",
                "description": "The original language code (e.g., 'en')."
              },
              "original_name": {
                "type": "string",
                "description": "The original name of the TV show."
              },
              "overview": {
                "type": "string",
                "description": "A brief overview or synopsis of the TV show."
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
                "description": "The media type, typically 'tv'."
              },
              "genre_ids": {
                "type": "array",
                "description": "An array of genre IDs for the TV show.",
                "items": {
                  "type": "integer"
                }
              },
              "popularity": {
                "type": "number",
                "description": "The popularity score of the TV show."
              },
              "first_air_date": {
                "type": "string",
                "description": "The first air date of the TV show (format: YYYY-MM-DD)."
              },
              "vote_average": {
                "type": "number",
                "description": "The average vote rating."
              },
              "vote_count": {
                "type": "integer",
                "description": "The number of votes."
              },
              "origin_country": {
                "type": "array",
                "description": "An array of origin country codes (e.g., 'US').",
                "items": {
                  "type": "string"
                }
              }
            },
            "required": [
              "adult",
              "backdrop_path",
              "id",
              "name",
              "original_language",
              "original_name",
              "overview",
              "poster_path",
              "media_type",
              "genre_ids",
              "popularity",
              "first_air_date",
              "vote_average",
              "vote_count",
              "origin_country"
            ]
          }
        },
        "total_pages": {
          "type": "integer",
          "description": "The total number of pages."
        },
        "total_results": {
          "type": "integer",
          "description": "The total number of results."
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

    url = f"https://api.themoviedb.org/3/trending/tv/{time_window}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
