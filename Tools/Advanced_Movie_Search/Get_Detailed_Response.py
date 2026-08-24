import os
import requests

def Get_Detailed_Response(movie_id):
    """
    :API_description: Retrieve comprehensive details about a specific movie, including budget, revenue, genres, and more.
    :param movie_id: The unique identifier for the movie whose details are to be fetched.
    :response_schema: 
    ```json
    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "adult": {
          "type": "boolean"
        },
        "backdrop_path": {
          "type": "string"
        },
        "belongs_to_collection": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "poster_path": {
              "type": "string"
            },
            "backdrop_path": {
              "type": "string"
            }
          },
          "required": ["id", "name", "poster_path", "backdrop_path"]
        },
        "budget": {
          "type": "integer"
        },
        "genres": {
          "type": "array",
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
            "required": ["id", "name"]
          }
        },
        "homepage": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "imdb_id": {
          "type": "string"
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
          "type": "string"
        },
        "production_companies": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "logo_path": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "origin_country": {
                "type": "string"
              }
            },
            "required": ["id", "logo_path", "name", "origin_country"]
          }
        },
        "production_countries": {
          "type": "array",
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
            "required": ["iso_3166_1", "name"]
          }
        },
        "release_date": {
          "type": "string"
        },
        "revenue": {
          "type": "integer"
        },
        "runtime": {
          "type": "integer"
        },
        "spoken_languages": {
          "type": "array",
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
            "required": ["english_name", "iso_639_1", "name"]
          }
        },
        "status": {
          "type": "string"
        },
        "tagline": {
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
        "adult", "backdrop_path", "belongs_to_collection", "budget", "genres", "homepage", "id", "imdb_id", "original_language", "original_title", "overview", "popularity", "poster_path", "production_companies", "production_countries", "release_date", "revenue", "runtime", "spoken_languages", "status", "tagline", "title", "video", "vote_average", "vote_count"
      ]
    }
    ```
    """
    url = "https://advanced-movie-search.p.rapidapi.com/api/movies/getdetails"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"movie_id": movie_id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "advanced-movie-search.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")