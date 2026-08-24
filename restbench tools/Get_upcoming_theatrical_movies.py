import os
import requests


def Get_upcoming_theatrical_movies(region=None):
    """
    :API_description: Get a list of upcoming movies in theatres. This is a release type query that looks for all movies that have a release type of 2 or 3 within the specified date range.

You can optionally specify a `region` prameter which will narrow the search to only look for theatrical release dates within the specified country.
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
              "description": "Maximum release date"
            },
            "minimum": {
              "type": "string",
              "description": "Minimum release date"
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
                "type": "boolean"
              },
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Backdrop image path"
              },
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "description": "Array of genre IDs"
              },
              "id": {
                "type": "integer"
              },
              "original_language": {
                "type": "string"
              },
              "original_title": {
                "type": "string"
              },
              "overview": {
                "type": "string"
              },
              "popularity": {
                "type": "number"
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "release_date": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "video": {
                "type": "boolean"
              },
              "vote_average": {
                "type": "number"
              },
              "vote_count": {
                "type": "integer"
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
          "type": "integer"
        },
        "total_results": {
          "type": "integer"
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

    url = "https://api.themoviedb.org/3/movie/upcoming"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = {"region": region}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
